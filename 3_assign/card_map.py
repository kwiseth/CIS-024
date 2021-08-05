#!/usr/bin/python3.6/card_map.py

"""Exercise P3.14. User enters a two-character notation for a specific playing
card and its suit and the script displays the full description of the card.
"""

SUITS = {'C':'Clubs', 'D':'Diamonds', 'H':'Hearts', 'S':'Spades'}
FACE_CARDS = {'A':'Ace', 'J':'Jack', 'K':'King', 'Q':'Queen'}
PLAIN_CARDS = {'1':'One', '2':'Two', '3':'Three', '4':'Four', '5':'Five',\
 '6':'Six', '7':'Seven', '8':'Eight', '9':'Nine', '10':'Ten'}

card_notation = input("Enter the card notation: ").upper()

if len(card_notation) > 2:
    card_val = card_notation[0] + card_notation[1]
    suit_val = card_notation[2]
    if not card_val in PLAIN_CARDS and not card_val in FACE_CARDS or not suit_val in SUITS:
        exit("Please enter a valid playing card notation, eg, 'QS' for Queen of Spades.")
    else:
        print(PLAIN_CARDS[card_val], "of", SUITS[suit_val])

if len(card_notation) == 2:
    card_val = card_notation[0]
    suit_val = card_notation[1]
    if not card_val in PLAIN_CARDS and not card_val in FACE_CARDS or not suit_val in SUITS:
        exit("Please enter a valid playing card notation, eg, 'QS' for Queen of Spades.")
    else:
        if card_val in FACE_CARDS:
            print(FACE_CARDS[card_val], "of", SUITS[suit_val])
        elif card_val in PLAIN_CARDS:
            print(PLAIN_CARDS[card_val], "of", SUITS[suit_val])
