import string

alphabet = list(string.ascii_lowercase)
alphabet.extend(alphabet)

def user_input():
  while True:
    try:
      direction = input("Please choose which you would like to perform...\n0 - encode\n1 - decode\n")
      assert direction in ['0','1']
    except ValueError:
          print("Not in the options given. Please choose again.")
    except AssertionError:
          print("Not in the options given. Please choose again.")
    else:
        break
    
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  
  return direction, text, shift

def caesar(text, shift, direction):
  original_txt = list(text)
  final_txt = str()

  if direction == '1':
    shift *= -1  # make the shift become negative
  
  for letter in original_txt:
    if letter in alphabet: 
      letter_index = alphabet.index(letter)
      final_index = letter_index + (shift % 26)
      
      final_txt += alphabet[final_index]

    else:
      final_txt += letter

  print(f'The encoded text is {final_txt}')
