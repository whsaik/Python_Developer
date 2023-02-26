from replit import clear
import random
from hangman_words import word_list
import hangman_art

print(hangman_art.logo)
# define maximum of life of the hangman
life = 6 

# Randomly choose a word from the word_list
chosen_word = random.choice(word_list)
chosen_list = list(chosen_word)
tried_list = []
n = len(chosen_word)
results = list("_"*n)

# Ask the user to guess a letter 
while life > 0:
  print(hangman_art.stages[life])
  print(" ".join(results))
  guess_char = input("Guess your character: ").lower()
  
  # Check if the letter guessed before
  if guess_char not in tried_list:
    clear()
    tried_list.append(guess_char)
    
    if guess_char in chosen_word:
      for i in range(n):
        if guess_char == chosen_word[i]:
          results[i] = chosen_list[i]
        
    
      if "_" not in results:
        print(hangman_art.stages[life])
        print("You win!")
        print(f"The correct answer is {chosen_word}")
        break
      
    else:
      clear()
      life -= 1
      print(f"You guess {guess_char} which is not in list. You lose one life!")

  else:
    clear()
    print("You guessed this letter before. Try another letter.")

if life == 0:
  print(hangman_art.stages[life])
  print(f"The correct answer is {chosen_word}")
  print("You lose...\nGAME OVER")
