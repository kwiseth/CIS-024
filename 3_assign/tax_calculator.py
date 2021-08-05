#!/usr/bin/python3.6/tax_calculator.py

"""Exercise P3.25. Computes income tax due based on schedule in book. Tax rates
take into account Married or Single filing status. Rates also vary based on
three different income levels.
"""
# Initialize constant variables for the tax rates and rate limits.
RATE1 = 0.10
RATE2 = 0.15
RATE3 = 0.25
# These constants should be the threshold values between tax rates
RATE1_S_CAP = 8000.0
RATE2_S_CAP = 32000.0
RATE1_M_CAP = 16000.0
RATE2_M_CAP = 64000.0
BASE_TAX_RATE2_S = 800.0
BASE_TAX_RATE3_S = 4400.0
BASE_TAX_RATE2_M = 1600.0
BASE_TAX_RATE3_M = 8800.0

# Obtain income amount and filing status
income = float(input("Please enter your income: "))
filing_status = input("Please enter 's' for single or 'm' for married: ").lower()

total_tax = 0

# Calculate taxes due on the income amount based on filing status
if filing_status == "s" :
    if income < RATE1_S_CAP :
        total_tax = RATE1 * income
    elif income > RATE2_S_CAP :
        total_tax = BASE_TAX_RATE3_S + (income - RATE2_S_CAP) * RATE3
    else :
        total_tax = BASE_TAX_RATE2_S + (income - RATE1_S_CAP) * RATE2
elif filing_status == "m":
    if income < RATE1_M_CAP :
        total_tax = RATE1 * income
    elif income > RATE2_M_CAP :
        total_tax = BASE_TAX_RATE3_M + (income -RATE2_M_CAP) * RATE3
    else :
        total_tax = BASE_TAX_RATE2_M + (income - RATE1_M_CAP) * RATE2
elif filing_status != "m" or filing_status != "s":
    exit("Please enter 'm' for married or 's' for single.")

# Print the results.
print("The tax due is ${:,.2f}".format(total_tax))
