from replit import clear
import art
#HINT: You can call clear() to clear the output in the console.
print(art.logo)
print("Welcome to the secret auction program.")

decision = True
bid_dict = {}

while decision:
  name = input("What is your name: ")
  bid = int(input("What is your bid? $"))
  bid_dict[name] = bid
  
  other_bidder = input("Are there any bidder? [y/n]\n")

  if other_bidder == 'n':
    decision = False
  clear()

max_v = max(bid_dict.values())
for k,v in bid_dict.items():
  if v == max_v:
    winner = k
  
print(f"The winner is {winner} with a bid of ${max_v}.")
