# nested_loops.py

side = int(input("input the side dimension of the square: "))
print("understand the values we're dealing with...")

print("side is ...", side)
print("side + 1 is ...", side + 1)
print("side +2 is ...", side + 2)
print("side x 2 is ...", side * 2)
print("side * 2 - 1 is...", side * 2 -1)
print("column in range(6) would be... ", range(6))

for row in range(side):
    for col in range(side * 2 + 1 ): # add one to 2x input value to obtain last column num

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
