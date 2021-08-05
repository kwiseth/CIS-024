#!/usr/bin/python3.6/math_basics.py

"""Exercise P2.4. Script that prompts user for two integers and then exercises Python's math
library to perform basic summary calculations, printing the results.
"""

print("=" * 80)
print("Enter two different integers when prompted below to see the sum, difference,\n\
product, average, distance between the two numbers, and maximum and\nminimum values.")
print("=" * 80)

first_num = int(input("Enter the first integer: "))
second_num = int(input("Enter the second integer: "))

print("Sum is ", first_num + second_num)
print("Difference between first number and second is ", first_num - second_num)
print("Product is ", first_num * second_num)
print("Average of the two numbers is ", (first_num + second_num)/2)
print("Distance between the two integer numbers is ", abs(first_num - second_num))
print("Number with the maximum value is ", max(first_num, second_num))
print("Number with minimum value is ", min(first_num, second_num))
