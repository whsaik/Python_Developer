import crypting_fx
from art import logo

print(logo)
print("Welcome to the Caesar Cipher Program")

ans = True
while ans == True:
  direction, text, shift = crypting_fx.user_input()
  
  try:
    crypting_fx.caesar(text, shift, direction)
  
    cont = input("Do you wish to continue? [y/n]\n")
    assert cont in ['y', 'n']

    if cont == 'n':
      ans = False
  except ValueError:
        print("Not in the options given. Please choose again.")
  except AssertionError:
        print("Not in the options given. Please choose again.")
