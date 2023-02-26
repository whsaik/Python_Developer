from replit import clear
from art import logo

# Addition
def add(n1, n2):
  return n1 + n2

# Subtraction
def minus(n1, n2):
  return n1 - n2

# Multiplication
def multiply(n1, n2):
  return n1 * n2

# Division
def div(n1, n2):
  return n1/n2

operations = {"+": add, "-": minus, "*": multiply, "/": div}

def calculator():
  print(logo)
  num1 = float(input("What is the first number: "))

  while True:
    for i in operations.keys():
      print(i)
    print("new\nend")
    ops = input("Which operation would you like to perform?")
    
    if ops == "new":
      clear()
      calculator()
    elif ops == "end":
      print("Bye~")
      return
      
    num2 = float(input("What is the second number: "))
    
    answer = operations[ops](num1, num2)
    
    print(f"{num1} {ops} {num2} = {answer}\n")
    num1 = answer

calculator()
