#!/usr/bin/python3.6/p4_35.py

"""Exercise P4.35. Credit card number check. User enters 8-digit credit-card
number and the script validates the check digit by performing calculations defined
in the problem.
"""

# credit_card_num = int(input("Enter the credit card number: "))


# TODO add validation routine to check for valid numeric entry

credit_card_num = 98765432
VALID_VALUE = 0
actual_check_digit_value = 0

print("Credit card number is ", credit_card_num)

print("last digit of number using modulo % ", credit_card_num % 10)

print("convert to list and use list comprehension to total")

digits = [int(x) for x in str(credit_card_num)]
print(digits)


print("The list consists of these digits ", digits)

print("last digit using index at last in list ", digits[len(digits)-1])
print("2nd digit from end is ", digits[len(digits)-2])

#print(sum(digits[i] for i in range(len(digits)-1, 0, -2)))
#sum_1 = (sum(digits[i] for i in range(len(digits)-1, 0, -2))) # list comprehension

sum_1 = 0
test1 = range(len(digits)-1, 0, -2)
print("test1 is ", test1)
for i in range(len(digits)-1, 0, -2):
    print(digits[i])
    sum_1 += (digits[i])
print("sum of digits using negative range is ...", sum_1)

sum_1a = 0
test1a = range(1, len(digits)-1, 2)
for i in range(1, len(digits), 2):
    print(digits[i])
    sum_1a += (digits[i])
print("sum of digits using positive range is ", sum_1a)


print("now double remaining numbers and extract digits comprising each, then add")
sum_2 = 0

print(sum_2)

test2 = range(len(digits)-2, -1, -2)
print("Test 2 is ...", test2)

sum_2a = 0
for i in range(len(digits)-2, -1, -2):
    print("inside the second for loop...")
    print("digits[i] is ..", digits[i])
    sum_2 += digits[i]
print("testing negative range only, not final results... sum_2 is", sum_2)
#    print(2*digits[i])
#    print("now add each individual digit")
#    print("digits[i] should be: ", 2*digits[i] % 10 + 2*digits[i] %10 //10)

for i in range(0, len(digits)-1, 2):
    print(digits[i])
    sum_2a += digits[i]
print("testing positive range vs negative range... sum_2a is ... ", sum_2a)


"""
print(sum_2)

total = sum_1 + sum_2
print(total)
actual_check_digit_value = (total % 10)

if actual_check_digit_value == VALID_VALUE:
    print("Credit card is valid")
else:
    print("credit card number not valid")
    print("check digit on number should be changed to ")
    """

#    print(VALID_VALUE - actual_check_digit_value) + (credit_card_num % 10) # FIXME
