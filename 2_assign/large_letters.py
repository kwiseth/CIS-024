#!/usr/bin/python3.6/large_letters.py

"""Exercise P2.18. Script that creates large letters and then prints the
word "HELLO" using each letter. Each letter is defined as a constant.
"""

LETTER_H = "*   *\n*   *\n*****\n*   *\n*   *\n\n"
LETTER_E = "*****\n*\n*****\n*\n*****\n\n"
LETTER_L = "*\n*\n*\n*\n*****\n\n"
LETTER_O = " *** \n*   *\n*   *\n*   *\n *** \n"

print("\n" + LETTER_H + LETTER_E + (2 * LETTER_L) + LETTER_O)
