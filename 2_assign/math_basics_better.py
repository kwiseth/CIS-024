#!/usr/bin/python3.6/math_basics_better.py

"""Exercise P2.5. Script that prompts user for two integers and then exercises
Python's math library to perform basic summary calculations, printing the results.
Script uses format operator.
"""

print("\nEnter two different integers as prompted below to see the sum,\ndifference, \
product, average, distance between the two numbers, and\nmaximum and minimum \
values.\n")
print("=" * 60)

first_num = int(input("Enter the first integer:  "))
second_num = int(input("Enter the second integer:  "))
print("-" * 60, "\n")
print("Sum:        %10d" % (first_num + second_num))
print("Difference: %10d" % (first_num - second_num))
print("Product:    %10d" % (first_num * second_num))
print("Average:    %13.2f" % ((first_num + second_num)/2))
print("Distance:   %10d" % (abs(first_num - second_num)))
print("Maximum:    %10d" % (max(first_num, second_num)))
print("Minimum:    %10d" % (min(first_num, second_num)))

print("-" * 60, "\n")
