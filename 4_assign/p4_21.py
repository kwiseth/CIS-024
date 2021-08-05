#!/usr/bin/python3.6/p4_21.py

"""Exercise P4.21. User enters an integer and script displays adjacent filled
and hollow squares in asterisks. Dimensions are sized using the value of the
integer entered.
"""

side = int(input("Enter an integer value for the size of the square: "))

# Columns will be twice the number of rows plus 1 for space between the two squares.

for row in range(side):
    # add one to 2x input value to obtain last column num
    for col in range(side * 2 + 1 ):
        # this prints the solid square with asterisks
        if ((col < side) and (row >= 0 or row <= side - 1)):
            print("*", end="")

        # this provides the gutter between the solid and the outline square
        if (col == side) and (row >= 0 or row <= side - 1):
            print(" ", end="")

        #  this prints the asterisks at the top and bottom rows of the outline square
        if (row == 0 or row == side - 1) and (col >= side + 1):
            print("*", end="")

        # this should print the two vertical bars that make up the outside of the square
        if ((col == side + 1) or (col == side * 2)) and (row > 0 and row < side - 1):
            print("*", end="")

        # this should fill in the middle of the open square with space
        if ((col > side + 1) and (col < side * 2)) and (row > 0 and row < side - 1):
            print(" ", end="")

    print()
