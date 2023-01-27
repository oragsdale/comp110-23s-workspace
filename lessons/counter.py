"Demonstrates how to count something"

number_string: str = "321"
number_of_odds: int = 0

#if a number % 2 == 1 then it is odd
if int(number_string[0]) % 2 == 1:
    print("odd!")
    number_of_odds += 1

print(number_of_odds)

