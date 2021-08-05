#testing_loops.py



"""        if col == side:
            print("*", end="")
        if col == side + 1:
            print(" ", end = "")
        if row == 0 or row == side - 1 and (col >= side + 2):
            print("*", end = "")
        if row > 0 or row < side - 1 and (col == side + 1):
            print("*", end = "")
        if row > 0 or row < side - 1 and col == 2 * side - 1:
            print("*", end = "")


"""
        """
            and (row >= 0 or row <=side)) or\
         ((col >= side + 2 or col <= 2 * side + 1) and (row == 0 or row == side - 1)):
            print("*", end = "")
        if (col == side + 2) and (row >= 1 or row <= side - 1):
            print("*", end = "")
        if (col == 2 * side - 1) and (row >= 0 or row <= side -1):
            print("*", end = "")
"""
        #if row == 0 or row == side - 1:
             #print("*", end = "")
#    print()
#    print()

"""
for row in range(side):
    for col in range(side + 2, 2 * side - 1):
#        if row == 0 or row == side -1 and col >= 0 and col <= side:
#            print("*", end = "")
        if (col == side + 2 or col == 2 * side - 1) and row == 0 or row == side - 1:
            print("*", end = "")
        else:
            print(" ", end = "")
    print()
"""

"""
for i in range(side) :
    for j in range(side) :
        for k in range(side * 2 -1):
            print(i, "\t", j, "\t", k, "\t", end="")
        for k in range(side + 1) :
            print(i, "\t", j, "\t", k, "\t", end="")
        for k in range(side * 2 - 1):
            print(i, "\t", j, "\t", k, "\t", end="")
        print()

FIRST_ROW = 0
LAST_ROW = side - 1
FIRST_COL = 0
LAST_COL = side - 1

for row in range(side):
    for col in range(side):
        if row == FIRST_ROW or row == LAST_ROW or\
         col == FIRST_COL or col == LAST_COL:
            print("*", end = "")
        else:
            print(" ", end="")
    print()

FIRST_ROW = 0
LAST_ROW = side - 1
FIRST_COL = (side * 2) + 1
LAST_COL = (FIRST_COL + side)
print(FIRST_ROW, "\t", FIRST_COL)
print(LAST_ROW, "\t", LAST_COL)

for row in range(side):
    for col in range((side * 2) + 1):
        if row == FIRST_ROW or row == LAST_ROW or col == FIRST_COL or\
         col == LAST_COL:
            print("*", end = "")
        else:
            print(" ", end = "")
print()

"""



# Python Program to Print Hollow Square Star Pattern
"""
side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern")
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
"""
