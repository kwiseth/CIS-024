#!/usr/bin/python3.6/p4_35.py

"""Exercise P4.35. Credit card number check. User enters 8-digit credit-card
number and the script validates the check digit by performing calculations defined
in the problem. 
"""

valid_entry = False

while not valid_entry :
    credit_card_num = input("Enter an 8-digit credit card number: ")
    if credit_card_num.isdigit() and len(credit_card_num) ==8:
        credit_card_num = int(credit_card_num)
        valid_entry = True
    else:
        print("Please try again. Only series of 8 numbers allowed. ")

VALID_VALUE = 0
actual_check_digit_value = 0

"""Create a list of numbers from the credit card number entered by the user
makes it simpler and more explicit to implement the algorithm. Using list
comprehension to create the list."""

digits = [int(num) for num in str(credit_card_num)]
FINAL_DIGIT = digits[len(digits)-1]
PENULTIMATE_DIGIT = digits[len(digits)-2]

""" Summing the alternating digits starting with the FINAL_DIGIT and moving
to the beginning of the list in steps of -2 until complete. Using list
comprehension (which unfortunately, Horstmann does not cover in his book)."""

sum_1 = 0
sum_1 = (sum(digits[i] for i in range(len(digits)-1, 0, -2)))

""" Doubling the alternating digits not used in prior calculation, and then
adding up the distinct digits that make up those doubled amounts. Requires
using floor division with modulo and modulo to obtain final and
penultimate digits from each of the four doubled numbers."""

sum_2 = 0

for i in range(len(digits)-2, -1, -2):
    sum_2 += (digits[i] * 2 // 10) % 10 + digits[i] * 2 % 10
print("sum_2 is ... ", sum_2)
total = 0
total = sum_1 + sum_2

actual_check_digit_value = (sum_1 + sum_2) % 10
if actual_check_digit_value == VALID_VALUE:
    print("Credit card is valid.")
else:
    print("The credit card number not valid.")
    change_digit_val = 0
    for num in range(1,10):
        adj_sum_1 = (sum_1 - FINAL_DIGIT) + num
        if ((adj_sum_1 + sum_2) % 10) == 0:
            change_digit_val = num
            print("To make credit card number", credit_card_num, "valid, change ", end="")
            print("final digit", FINAL_DIGIT, "to", change_digit_val)
