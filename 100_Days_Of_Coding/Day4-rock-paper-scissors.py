rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

results = [rock, paper, scissors]

n = random.randint(0, 2)

print("Welcome to the game of rock-paper-scissors!!!")
user = int(input("What do you choose?\n0 - rock\n1 - paper\n2 - scissors\n"))

print(results[user])
print(f"Computer choose...\n{results[n]}")

if user == n:
  print("Draw...")
elif user == 0 and n == 2:
  print("You WIN!!!")
elif user == 1 and n == 0:
  print("You WIN!!!")
elif user == 2 and n == 1:
  print("You WIN!!!")
else:
  print("You LOSE~~~")
