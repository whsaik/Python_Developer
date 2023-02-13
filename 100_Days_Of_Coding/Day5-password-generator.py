#Password Generator Project
import random
import string
#Get required list for letters, numbers and symbols
letters = list(string.ascii_letters)
numbers = list(string.digits)
symbols = list(string.punctuation)

#Asking user for their needs
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Generate random password
password =[]

for i in range(nr_letters):
  x = letters[random.randint(0, len(letters)-1)]  #can use random.choice() to randomly pick element from a list
  password.append(x)

for i in range(nr_symbols):
  x = symbols[random.randint(0, len(symbols)-1)]
  password.append(x)

for i in range(nr_numbers):
  x = numbers[random.randint(0, len(numbers)-1)]
  password.append(x)

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
print("".join(password))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
hard_pass = []

#Randomised the order of the password
for k in range(len(password)):  #can use the list.shuffle() to shuffle the list
  a = password.pop(random.randint(0, len(password)-1))
  hard_pass.append(a)

print("".join(hard_pass))
