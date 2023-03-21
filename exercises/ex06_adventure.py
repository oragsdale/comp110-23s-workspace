"""In this program the user will play a game of volleyball to 5."""

__author__ = "730560351"

from random import randint
# globals
points: int = 0
player: str = ""
COWBOY = "\U0001F920"


def greet() -> None:
    """greet greets the user, and prompts them for their name."""
    global player
    print(f"\nGreetings! Welcome to virtual vball! This game is a simulation of real life indoor volleyball.")
    player_name: input(str) = input("What is the users name? ")
    player = player_name
    

def rally() -> None:
    """rally is run when a serve is recieved by the other team and the ball is in play. This will always go back to the serve."""
    global points
    swing: int = randint(0, 10)
    recieve: input(str) = input("\nThe other team received your serve. The ball is coming your way! Do you want to hit from the... \noutside \nopposite \nmiddle \n")

    if recieve.lower == "outside" or "opposite":
        if swing < 3:
            print("You got blocked! Serve again.")
        elif swing > 3 and swing < 8: 
            print(f"Way to go {player}! It's a kill {COWBOY}")
            points += 1
        elif swing >= 8:
            print("You swung out. Serve again!")

    if recieve.lower == "middle":
        if swing < 4:
            print("You got blocked! Serve again.")
        else: 
            print(f"Way to go {player}! It's a kill {COWBOY}")
            points += 1


def top() -> None:
    """top gives a random result following the user choosing to top spin serve."""
    global points
    serve: int = randint(0, 10)
    if serve <= 2:
        print(f"\nAce! Way to go {player}, you earned one point.")
        points += 1
    elif serve < 7 and serve > 2:
        print("\nThe ball is in!")
        rally()
    elif serve >= 7:
        print("\nYour serve was out. Serve again")


def power_float() -> None:
    """top gives a random result following the user choosing to top spin serve."""
    global points
    serve: int = randint(0, 10)
    if serve <= 2:
        print(f"\nAce! Way to go {player}, you earned one point.")
        points += 1
    elif serve < 9 and serve > 2:
        print("\nThe ball is in!")
        rally()
    elif serve >= 9:
        print("\nYour serve was out. Serve again")


def hybrid(score: int) -> int:
    """hybrid is the custom function. It recieves the points and determines whether or not the user is able to do a hybrid serve. This is high risk, so if the score is close to 5 hybrids are not allowed."""
    global points
    serve: int = randint(0, 10)
    if score < 4:
        if serve < 5:
            print(f"\nYou served an aggresive hybrid and it was an ace! Way to go {player}.")
            score += 1 
        else: 
            print("\nYou served an aggressive hybrid and it went out. Serve again!")
    else: 
        print("\nDon't serve hybrid when the game is this close! You're only one point away! Serve again.")

    return score


def main() -> None:
    """main runs each of the functions and procedures in a changing order based on the users decisions."""
    global points
    greet()
    playing = True
    while playing and points < 5: 
        start: input(str) = input("\nYou're serving first would you like to... \ntop spin \npower float \nhybrid \nend game \n")
        
        if start == "top spin":
            top()
        
        if start == "power float":
            power_float()

        if start == "hybrid":
            points = hybrid(points)
            
        if start == "end game":
            print(f"Thanks for playing {player}! you earned {points} points. So close!")
            playing = False

        print(f"points = {points}")

    if points == 5: 
        print(f"Congratulations!! You won the game {COWBOY}")


if __name__ == "__main__":
    main()