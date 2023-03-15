from tkinter import *
from tkinter import messagebox
from password_generator import password_generator
import pyperclip
import json

# ---------------------------- PASSWORD SEARCH ------------------------------- #
def pass_search():
    web = web_input.get()
    try:
        with open("data.json", "r") as file:
            data = json.load(file)
            if web in data:
                messagebox.showinfo(title=web, message=f"Email: {data[web]['Email']}\n"
                                        f"Password: {data[web]['Password']}")
            else:
                messagebox.showinfo(title=web, message=f"Password not found.")
                
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message=f"No password saved!!!")

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def pass_gen():
    password = password_generator()
    pass_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_pass():
    web = web_input.get()
    mail = user_input.get()
    password = pass_input.get()
    
    if len(web) == 0 or len(password) == 0:
        messagebox.showinfo(title="Attention!!!", message="Please don't leave any field empty.\nThank you.")
    
    else:
        new_data = {web:{"Email":mail, "Password": password}}
        
        Is_ok = messagebox.askokcancel(title=web, message=f"These are the details entered\nEmail: {mail}\n"
                                   f"Password: {password}\nIs it ok to save?")
        
        if Is_ok:
            try:
                with open('data.json', "r") as file:
                    data = json.load(file)
                    data.update(new_data)
            
            except FileNotFoundError:
                data = new_data  
            
            finally:
                with open('data.json', "w") as file:
                    json.dump(data, file, indent=4)
                    
                web_input.delete(0, END)
                pass_input.delete(0, END)
                web_input.focus()

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create canvas
canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

# Create label
web_label = Label(text="Website:", font=("Arial", 10))
web_label.grid(column=0, row=1)
web_label.config(padx=2,pady=2)

user_label = Label(text="Email/Username:", font=("Arial", 10))
user_label.grid(column=0, row=2)
user_label.config(padx=2,pady=2)

pass_label = Label(text="Password:", font=("Arial", 10))
pass_label.grid(column=0, row=3)
pass_label.config(padx=2,pady=2)

# User entry/ input
web_input = Entry(width=36)
web_input.grid(column=1, row=1)
web_input.focus()

user_input = Entry(width=55)
user_input.insert(0, "ak0326@gmail.com")
user_input.grid(column=1, row=2, columnspan=2)

pass_input = Entry(width=36)
pass_input.grid(column=1, row=3)

# Create button    
generate_button = Button(text="Generate Password", command=pass_gen)
generate_button.grid(column=2, row=3)

add_button = Button(text="Add", width=46, command=add_pass)
add_button.grid(column=1, row=4, columnspan=2)
add_button.config(padx=2, pady=2)

search_button = Button(text="Search", width=14, command=pass_search)
search_button.grid(column=2, row=1)
search_button.config(padx=2, pady=2)

window.mainloop()
