############### Blackjack Project #####################
import random
from art import logo
import bj_function
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
print(logo)
print("Welcome to our Blackjack Game")

p_deck, h_deck = [], []

# get 2 cards for each 
for i in range(2):
  bj_function.add_card(p_deck)
  bj_function.add_card(h_deck)

# display the current deck and score
score = bj_function.count_point(p_deck)
print(f"Your current deck is {p_deck}  score: {score}")
print(f"Dealer current deck is [{h_deck[0]}, X]")

# player turn(s) to get card(s)
while True:
  if len(p_deck) < 5:
    decision = input("Do you need an extra card? [y/n]\n")
    if decision == 'n':
      break
    else:
      bj_function.add_card(p_deck)
      score = bj_function.count_point(p_deck)
      print(f"Your current deck is {p_deck}  score: {score}")
      print(f"Dealer current deck is [{h_deck[0]}, X]")

  # check whether player has busted
  if score > 21:
    print("BOOOOOM!!!!!!!\nBUSTED!!!\nYOU LOSE")
    break

if score < 21:  
  # get extra card for dealer if it has small points
  while bj_function.count_point(h_deck) < 19 and len(h_deck) < 5 and bj_function.count_point(h_deck) <= score:
    bj_function.add_card(h_deck)
  
  # check the winner
  bj_function.win_check(p_deck, h_deck)
