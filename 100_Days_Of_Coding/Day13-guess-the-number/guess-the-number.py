# Guss the number game
from art import logo
import game_function as gf
import random
from replit import clear

dd = True
# Looping the game until the user want to stop
while dd == True:
  # starting and greeting
  print(logo)
  print("Welcome to the Game: Guess the Number!!!")
  print("I'm thinking of a number between 1 and 100. Can you guess what is it?")
  
  # asking for user input
  attempts = gf.get_dif()
  print(f"You have {attempts} attempts remaining to guess the number.")
  
  # random generate number to be guessed
  computer_number = random.randint(1,100)
  
  # start the guessing game
  gf.make_guess(computer_number, attempts)

  # ask the user whether to continue a new game or stop the game
  d = True
  while d == True:
    decision = input("Would you like to start a new game or stop the game? [y/n] ")
    if decision == 'n':
      print("Thank you for playing the game.\nHope to see you again.\nHave a nice day.n Bye ~ (^ o ^) ~")
      dd = False
      d = False
    elif decision == 'y':
      d = False
      clear()
    else:
      print("This is not in the options. Please try again...")

