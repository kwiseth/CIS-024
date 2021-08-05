#!/usr/bin/python3.6/roman_numerals.py

"""Exercise P3.28. User enters up to 4 digits and the script converts to Roman
numerals. Maximum value supported is 3,999.
"""

ROM_1 = "I"
ROM_5 = "V"
ROM_10 = "X"
ROM_50 = "L"
ROM_100 = "C"
ROM_500 = "D"
ROM_1000 = "M"

integer = int(input("Enter a positive integer (maximum value is 3,999): "))

# Tease out the digits that will be converted. 

ones = integer % 10
tens = (integer // 10) % 10
hundreds = (integer // 100) % 10
thousands = (integer // 100) // 10

""" Debugging and testing code 
print("ones count is  ... ", ones)
print("tens count is ... ", tens)
print("hundreds count is ...", hundreds)
print("thousands count is ...", thousands)
"""

if ones <= 3:
    roman_ones = ones * ROM_1
elif ones >= 5 and ones < 9:
    roman_ones = ROM_5 + (ones - 5) * ROM_1
elif ones == 4:
    roman_ones = ROM_1 + ROM_5
else:
    roman_ones = ROM_1 + ROM_10

if tens <= 3:
    roman_tens = tens * ROM_10
elif tens >= 5 and tens < 9:
    roman_tens = ROM_50 + (tens - 5) * ROM_10
elif tens == 4:
    roman_tens = ROM_10 + ROM_50
else:
    roman_tens = ROM_10 + ROM_100

if hundreds <= 3:
    roman_hundreds = hundreds * ROM_100
elif hundreds >= 5 and hundreds < 9:
    roman_hundreds = ROM_500 + (hundreds - 5) * ROM_100
elif hundreds == 4:
    roman_hundreds = ROM_100 + ROM_500
else:
    roman_hundreds = ROM_100 + ROM_1000

if thousands <= 3:
    roman_thousands = thousands * ROM_1000

print(roman_thousands + roman_hundreds + roman_tens + roman_ones)
