# higher or lower game
# import library
import art
from replit import clear
import game_data
import random

# checking who has higher follower, correct guess or not
def game_check(p1, p2, guess):
  if p1['follower_count'] > p2['follower_count'] and guess == "A":
    return True
  elif p1['follower_count'] < p2['follower_count'] and guess == "B":
    return True
  else:
    return False

# greeting of the game
print(art.logo)
print("Welcome to the game of \"Higher or Lower\"")
print("You will need to guess the person given has higher followers on Instagram or not")
print("Hope you enjoy the game~")

# define useful variable
points = 0

# randomly select from list
p1 = random.choice(game_data.data)
p2 = random.choice(game_data.data)

def game(p1, p2, points):
  # avoid same selection of p1 and p2
  while p2 == p1:
    p2 = random.choice(game_data.data)
  
  # display and ask user input for guess
  print(f"Compare A: {p1['name']}, a {p1['description']}, from {p1['country']}.")
  print(art.vs)
  print(f"against B: {p2['name']}, a {p2['description']}, from {p2['country']}.")
  
  while True:
    guess = input("Who has more followers? Type 'A' or 'B'\n")
    if guess == "A" or guess == "B":
      break
    else:
      print("Not in the option...\nTry again...")
  
  # check whether the guess is correct or not
  results = game_check(p1, p2, guess)
  
  if results == True:
    points += 1
    p1 = p2
    clear()
    print(art.logo)
    print(f"You're right, current score = {points}.")
    game(p1, p2, points)
  else:
    print(f"Sorry wrong guess, final score = {points}.")

game(p1, p2, points)
