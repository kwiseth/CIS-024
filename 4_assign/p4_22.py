#!/usr/bin/python3.6/p4_22.py

"""Exercise P4.22. Script prompts user to enter an integer. The script then
displays a filled diamond comprised of asterisks of the specified side length by
using nested for loops to print the top-half of the diamond and then the bottom
half of the diamond. 
"""

side_value = int(input("Enter an integer value for the side of the diamond: "))


# Print empty spaces and stars in increasing values going from top to mid-point
# of diamond shape, as defined by the side_value
for row in range(side_value):
    for blank_col in range(side_value - row):
        print(" ", end="")
    for star_col in range(row * 2 - 1):
        print("*", end="")
    print()
# Descend downwards from this point using the converse of the above, starting
# from widest line narrowing downward.
for row in range(side_value, 0, -1):
    for blank_col in range(side_value - row):
        print(" ", end="")
    for star_col in range(row * 2 - 1):
        print("*", end="")
    print()
