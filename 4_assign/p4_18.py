#!/usr/bin/python3.6/p4_18.py

"""Exercise P4.18 Prints a multiplication table for numbers 1 through 10.
"""

ROWS = 10
COLUMNS = 10

for row in range(1, ROWS + 1):
    for col in range(row, row * COLUMNS + 1, row):
        print("%5d" % col, end="")
    print()
