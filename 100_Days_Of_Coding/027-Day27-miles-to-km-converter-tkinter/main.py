import tkinter as tk

window = tk.Tk()
window.title("Mile to Km Converter")
# window.minsize(width=300, height=100)
window.config(padx=20, pady=20)

# user input miles
user = tk.Entry(width=10)
user.insert(tk.END, string="0")
user.grid(column=1, row=0)

# labels
label1 = tk.Label(text="Mile", font=("Arial", 10, "italic"))
label1.grid(column=2, row=0)

label2 = tk.Label(text="is equal to", font=("Arial", 10))
label2.grid(column=0, row=1)

label3 = tk.Label(text="km", font=("Arial", 10, "italic"))
label3.grid(column=2, row=1)

label4 = tk.Label(text="0", font=("Arial", 10))
label4.grid(column=1, row=1)

# define function to convert mile to km
def mile_to_km():
    n = float(user.get())
    ans = n * 1.609344
    label4.config(text=f"{ans:.2f}")

# Button
button = tk.Button(text="Calculate", command=mile_to_km)
button.grid(column=1, row=2)

window.mainloop()