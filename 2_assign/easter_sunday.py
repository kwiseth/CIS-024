#!/usr/bin/python3.6/easter_sunday.py

"""Exercise P2.21. Script that prompts user for a year and then calculates the
date (month and day) on which Easter Sunday would have fallen in the given year.
Uses an algorithm developed by Gauss. Tested using various dates, eg., 2013
which yielded March 31.
"""

print("=" * 80)
print("Enter a year (yyyy) to see the month and date on which Easter Sunday\n\
fell in that year.\n")
print("=" * 80)

y = int(input("Enter four digits for the year (yyyy): "))
a = y % 19
b = y // 100
c = y % 100
d = b // 4
e = b % 4
g = (8 * b + 13) // 25
h = (19 * a + b - d - g + 15) % 30
j = c // 4
k = c % 4
m = (a + 11 * h) // 319
r = (2 * e + 2 * j - k - h + m + 32) % 7
n = (h - m + r + 90) // 25
p = (h - m + r + n + 19) % 32

if n == 4:
    print("In", y, "Easter Sunday fell on April", p)
elif n == 3:
    print("In", y, "Easter Sunday fell on March", p)
else:
    print("In", y, "Easter Sunday fell on", n, p)
