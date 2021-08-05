#!/usr/bin/python3.6/taxes_1913.py

"""Exercise P3.23. Computes income tax due based on the 1913 six-tier tax schedule.
"""


# Initialize constant variables for the tax rates and some threshold mins and max.
RATE1 = 0.01
RATE2 = 0.02
RATE3 = 0.03
RATE4 = 0.04
RATE5 = 0.05
RATE6 = 0.06
RATE1_MIN = 0.0
RATE1_MAX = 50000.0
RATE2_MIN = 50001.0
RATE2_MAX = 75000.0
RATE3_MIN = 75001.0
RATE3_MAX = 100000.0
RATE4_MIN = 100001.0
RATE4_MAX = 250000.0
RATE5_MIN = 250001.0
RATE5_MAX = 500000.0
RATE6_MIN = 500001.0


valid_entry = False

# read income, after first checking that the entry is numeric before processing.
while not valid_entry :
    income = input("Please enter your income (whole numbers only): ")
    if income.isdigit():
        income = float(income)
        valid_entry = True
    else:
        print("Please try again. ")


# Read income
# income = float(input("Please enter your income: "))

# Compute taxes due.
tax_total = 0

if income <= RATE1_MAX:
    tax_total = RATE1 * income
elif income >= RATE6_MIN:
    tax_total = RATE6 * (income - RATE6_MIN) + RATE5 * (RATE5_MAX - RATE5_MIN)\
    + RATE4 * (RATE4_MAX - RATE4_MIN) + RATE3 * (RATE3_MAX - RATE3_MIN)\
    + RATE2 * (RATE2_MAX - RATE2_MIN) + RATE1 * (RATE1_MAX - RATE1_MIN)
elif income >= RATE5_MIN and income <= RATE5_MAX:
    tax_total = RATE5 * (income - RATE5_MIN) + RATE4 * (RATE4_MAX - RATE4_MIN)\
     + RATE3 * (RATE3_MAX - RATE3_MIN) + RATE2 * (RATE2_MAX - RATE2_MIN)\
     + RATE1 * (RATE1_MAX - RATE1_MIN)

elif income >= RATE4_MIN and income <= RATE4_MAX:
    tax_total = RATE4 * (income - RATE4_MIN) + RATE3 * (RATE3_MAX - RATE3_MIN)\
     + RATE2 * (RATE2_MAX - RATE2_MIN) + RATE1 * (RATE1_MAX - RATE1_MIN)

elif income >= RATE3_MIN and income <= RATE3_MAX:
    tax_total = RATE3 * (income - RATE3_MIN) + RATE4 * (RATE4_MAX - RATE4_MIN)\
     + RATE2 * (RATE2_MAX - RATE2_MIN) + RATE1 * (RATE1_MAX - RATE1_MIN)

else: # rate2 must apply at this point
    tax_total = RATE2 * (income - RATE2_MIN) + RATE1 * (RATE1_MAX - RATE1_MIN)

# Print the amount of total tax.
print("In 1913, the US income tax on an income of ${:,.2f}".format(income),\
"would have been $%.2f" % tax_total)
