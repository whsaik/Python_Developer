def get_dif():
  '''
  Asking user for their input to select the difficulty of the game.
  Return the number of attempts
  '''
  while True:
    difficulty = input("Choose a difficulty.\n0 - Easy\n1 - Hard\n")

    if difficulty == '0':
      attempts = 10
      break
    elif difficulty == '1':
      attempts = 5
      break
    else:
      print("This is not the options. Please try again.")
      
  return attempts

def make_guess(computer_number, attempts):
  '''
  First get the input from user about the guess and compare with the correct answer. 
  
  Then, will continue until the correct answer is guessed or no more attempts left.
  '''
  while attempts > 0:
    guess = int(input("Make a guess: "))
    if guess == computer_number:
      print("You're CORRECT! \nYOU WIN!!!")
      return
    else:
      print("Wrong guess!!!")
      if guess > computer_number:
        print("Too high!")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")
      elif guess < computer_number:
        print("Too low!")
        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

  if attempts == 0:
    print(f"The correct answer is {computer_number}\nYOU LOSE!!!")
