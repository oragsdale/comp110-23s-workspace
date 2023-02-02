"""demonstrates while loops by finding low value in string"""

card: str = "5235"

card_idx: int = 0
low_card: int = int(card[0])
while card_idx < 4:
    # check if current card is less than low card
    current_card: int = int(card[card_idx])
    if current_card < low_card:
        # update the low card to be the value of our current card
        low_card = current_card
    card_idx += 1
print(low_card)