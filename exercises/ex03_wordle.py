"""This program contains a more structured wordle game, which implements functions and only 6 guesses."""
__author__ = "730560351"

def contains_char(guess: str, char: str) -> bool:
    """contains_char has two perimeters as strings. The function checks if the second string is found in the first one, then returns True if this is true, or False otherwise."""
    assert len(char) == 1 
    idx = 0

    # This while loop compares the character recieved to each character of the guess. If the character is in the guess True is returned. False is returned otherwise
    while idx < len(guess): 
        if char == guess[idx]:
            return True
        else: 
            idx += 1
        
    return False

def emojified(guess: str, secret: str) -> str:
    """emojified examines whether characters of the guess are in the secret word using contains_char, then creates a display with a certain color box based on the characters position in the guess."""
    assert len(guess) == len(secret)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"  
    display: str = ""
    idx: int = 0

    # This while loop runs for each character in the guess
    while idx < len(guess):
        # The if statement runs if contains_char returns True. If contains_char returns False, then a white box is appended to the display. If True is the case, the if statement compares the exact characters of guess and secret to determine whether to add a yellow or green box to the display.
        if contains_char(secret, guess[idx]):
            if guess[idx] == secret[idx]:
                display += GREEN_BOX
            else: 
                display += YELLOW_BOX
        else: 
            display += WHITE_BOX
        idx += 1

    return display
        
def input_guess(expected_len: int):
    """This function prompts the user for a guess and insures that the guess is of proper length."""
    guess: str = input(f"Enter a {expected_len} character word: ")
    
    while len(guess) != expected_len:
        guess = input(f"That wasn't {expected_len} chars! Try again: ")
    
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    secret: str = "codes"
    win: bool = False
    
    # This while loop runs while the user has guessed fewer than 6 times, and have not won yet. 
    while turn <= 6 and win == False: 
        print(f"=== Turn {turn}/6 === ")
        guess: str = input_guess(5)
        display: str = emojified(guess, secret)
        print(display)
        if guess == secret:
            win: bool = True
            print(f"You won in {turn}/6 turns! ")
        
        turn += 1

    if win == False: 
        print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()