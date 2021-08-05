#!/usr/bin/python3.6/p4_23.py

"""Exercise P4.23 Play the game Nim against the computer. Computer plays in
one of two modes: basic (preferred word over pejorative 'stupid') or advanced
(also preferred word), chosen at random. The loser of the game is the player
who picks the last marble from the current pile.
"""

from random import randint


print("Welcome to the Nim game.")
response = input("Welcome to the Nim game. Press \"s\" to start (or \"q\" to quit): ").upper()

if response == 'Q':
    exit("Goodbye. Come back soon.")
elif response == 'S':
    pile = randint(10, 100)
    print("Let the game begin. The starting pile size is ", pile)


    MIN_PULL = 1
    max_pull = ( pile // 2 )

    player_pull = 0
    computer_pull = 0
    turn_ctr = 0

    # Sets the computer mode to basic(0) or advanced(1)
    mode = randint(0, 1)
    print(mode)

    if mode == 0:
        print("Computer will be playing in basic mode.")
    elif mode ==1:
        print("Computer will be playing in advanced mode.")

    # Determines whether computer goes first (0) or player (1)
    first_turn = randint(0, 1)
    print("first turn is..", first_turn)

    if first_turn == 0:
        print("Computer gets first turn to pull from the starting pile of", pile, "marbles.")
        if mode == 0:
            computer_pull = randint(1, pile // 2)
            pile = pile - computer_pull
            turn_ctr += turn_ctr + 1
        elif mode == 1:
            print("To do")
            # computer_pull = pile -
    else:
        print("You get first turn to pull from the starting pile of", pile, "marbles.")
        print("You can pick from", MIN_PULL, "up to", max_pull, "marbles.")
        player_pull = input("How many marbles would you like to take?: ")
        player_pull = int(player_pull)
        pile = pile - player_pull
    print("new pile size for next turn is...", pile)
