# 20/6/2023

# TODO: Create a letter using starting_letter.txt

with open("./Input/Names/invited_names.txt") as name_list:
    names = name_list.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as template:
    letter_template = template.read()

for name in names:
    with open(f"./Output/ReadyToSend/Letter to {name}.txt", "w") as letter:
        final_letter = letter_template.replace("[name]", name)
        final_letter = final_letter.replace("Angela", "Lulama")
        letter.write(final_letter)
