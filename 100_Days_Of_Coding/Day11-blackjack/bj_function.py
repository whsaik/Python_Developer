import random

def count_point(deck):
  points = 0
  ace_n = 0
  for i in deck:
    if i in ["J","Q","K"]:
      points += 10
    elif i == "A":
      ace_n += 1
    else:
      points += i

  if ace_n > 0:
    if points + 11 + (ace_n - 1) > 21:
      points = points + 1 + (ace_n - 1)
    else:
      points = points + 11 + (ace_n - 1)
  return points

def add_card(player_deck):
  card_list = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
  card = random.choice(card_list)
  return player_deck.append(card)

def win_check(p_deck, h_deck):
  p_points = count_point(p_deck)
  h_points = count_point(h_deck)
  if p_points > h_points or h_points > 21:
    print(f"Your current deck is {p_deck}  score: {p_points}")
    print(f"Dealer current deck is {h_deck}  score: {h_points}")
    print("You WIN!")
  elif p_points < h_points:
    print(f"Your current deck is {p_deck}  score: {p_points}")
    print(f"Dealer current deck is {h_deck}  score: {h_points}")
    print("You LOSE~")
  else:
    print(f"Your current deck is {p_deck}  score: {p_points}")
    print(f"Dealer current deck is {h_deck}  score: {h_points}")
    print("DRAW")
