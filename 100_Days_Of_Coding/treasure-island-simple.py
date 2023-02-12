print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("Let us start our journey~~~")
print("Friendly reminder!!!")
print("In our journey, our rules are strick!!!")
print("NO CHEATING NOR CHOOSE OUTSIDE THE OPTIONS GIVEN!!!")
print("Otherwise, painful judgement are waiting for you XD")
print("After a long walk, there are two ways to go...")
decision1 = input("You would like to turn left or turn right? L  R\n")
if decision1 == "L":
  print("You continue your journey...")
  print("There is a lake in front but the boat is yet to come back...")
  decision2 = input("You would like to swim over or wait for the boat? swim  wait\n")
  if decision2 == 'wait':
    print("The boat is back and you continue your journey...")
    print("You successfully over the lake, now there are three doors in front of you...")
    decision3 = input("Pick which door to open? Red  Blue  Yellow\n")
    if decision3 == "Yellow":
      print("You win!")
    elif decision3 == "Red":
      print("Burned by fire.\nGame Over.")
    elif decision3 == "Blue":
      print("Eaten by beasts.\nGame Over.")
    else:
      print("Game Over.")
  else:
    print("Attacked by trout.\nGame Over.")
else:
  print("Fall into a hole.\nGame Over.")
