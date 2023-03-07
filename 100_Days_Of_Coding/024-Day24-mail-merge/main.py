PLACEHOLDER = '[name]'

with open("./Input/Names/invited_names.txt","r") as name_file:
    name_list = name_file.readlines()
        
for person in name_list:

    with open(r".\Input\Letters\starting_letter.txt","r") as start_file:
        new_text = start_file.read().replace(PLACEHOLDER, person.strip())
        
    with open(f"./Output/ReadyToSend/letter_for_{person.strip()}.txt", "w") as f_file:
        f_file.write(new_text)                

                