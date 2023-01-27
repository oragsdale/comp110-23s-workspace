"""EX01 - Chardle - A cute step toward Wordle."""

__author__ = "730560351"

word_1: str = input("Enter a 5-character word: ")
if len(word_1) != 5: 
    print("Error: Word much contain 5 characters")
    exit()

character_1: str = input("Enter a single character: ")
if len(character_1) != 1: 
    print("Error: Character must be a single character.")
    exit()

num_characters: int = 0

print("Searching for " + character_1 + " in " + word_1)

if word_1[0] == character_1:
    print(character_1 + " found in index 0")
    num_characters += 1

if word_1[1] == character_1:
    print(character_1 + " found in index 1")
    num_characters += 1

if word_1[2] == character_1:
    print(character_1 + " found in index 2")
    num_characters += 1

if word_1[3] == character_1:
    print(character_1 + " found in index 3")
    num_characters += 1

if word_1[4] == character_1:
    print(character_1 + " found in index 4.")
    num_characters += 1

else: 
    pass

if num_characters == 0:
    print("No instances of " + character_1 + " found in " + word_1)
else: 
    if num_characters == 1: 
        print(str(num_characters) + " instance of " + character_1 + " found in " + word_1)

    if num_characters > 1: 
        print(str(num_characters) + " instances of " + character_1 + " found in " + word_1)