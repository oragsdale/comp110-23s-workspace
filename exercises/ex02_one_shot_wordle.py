"""This program compares characters in a string guessed by the user to a pre-assigned string, then creates a display to show which characters are in the correct order."""

__author__: str = "730560351"

SECRET: str = "python"
guess: str = input(f"What is your { str(len(SECRET)) }-letter guess? ")

# This if block checks to make sure the guess the user inputs has the same number of characters as the pre-determined word.
if len(guess) < len(SECRET):
    guessing: bool = True
else: 
    guessing: bool = False

# This while loop allows the user to continue guessing words even if they are not the correct length.
while guessing: 
    guess: str = input(f"That was not { str(len(SECRET)) } letters! Try again: ")
    if len(guess) == len(SECRET): 
        guessing = False

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
character: int = 0 
display: str = ""

# This while loop creates the display of boxes by comparing individual characters within the string. This while loop continues until all characters have been compared.
while character < len(SECRET):
    if guess[character] == SECRET[character]:
        display += GREEN_BOX
    else: 
        if guess[character] in SECRET:
            display += YELLOW_BOX
        else:
            display += WHITE_BOX
    character += 1

print(display)

# This if block gives feedback to the user based on their guess, then either celebrates their success or encourages them to try again.
if guess != SECRET:
    print("Not quite. Play again soon!")
else: 
    print("Woo! You got it!")