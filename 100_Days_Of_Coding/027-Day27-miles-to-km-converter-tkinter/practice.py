import tkinter 

window = tkinter.Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=500)
window.config(padx=20,pady=20)

# Create label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "italic"))
my_label.grid(column=0, row=0)
my_label.config(padx=10,pady=10)

## change the text inside the label
my_label['text'] = 'This is the second text'
my_label.config(text='This is the third label',padx=10,pady=10)

# Create button
def button_f():
    user_text = user_input.get()
    print(user_text)
    my_label.config(text=user_text)
    
my_button = tkinter.Button(text="Click me", command=button_f)
my_button.grid(column=1, row=0)
my_button.config(padx=10,pady=10)


# User entry/ input
user_input = tkinter.Entry(width=30)
user_input.insert(tkinter.END, string="Some text to begin with")
user_input.grid(column=0, row=1)

#Text
text = tkinter.Text(height=5, width=30)
#Puts cursor in textbox.
text.focus()
#Adds some text to begin with.
text.insert(tkinter.END, "Example of multi-line text entry.\nThanks.")
#Get's current value in textbox at line 2, character 0
print(text.get("2.0", tkinter.END))
text.grid(column=1, row=1)
text.config(padx=10,pady=10)

#Spinbox
def spinbox_used():
    #gets the current value in spinbox.
    print(spinbox.get())
spinbox = tkinter.Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=0, row=2)

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = tkinter.Scale(from_=0, to=100, command=scale_used)
scale.grid(column=2, row=0)

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = tkinter.IntVar()
checkbutton = tkinter.Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=2, row=1)
checkbutton.config(padx=10,pady=10)

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = tkinter.IntVar()
radiobutton1 = tkinter.Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = tkinter.Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=1, row=2)
radiobutton1.config(padx=10,pady=10)
radiobutton2.grid(column=2, row=2)
radiobutton2.config(padx=10,pady=10)

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = tkinter.Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=3, row=0)

# keep the window active
window.mainloop()