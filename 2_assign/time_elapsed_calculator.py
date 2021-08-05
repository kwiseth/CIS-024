#!/usr/bin/python3.6/time_elapsed_calculator.py

"""Exercise P2.17. Lets user enter two military time values (0730, 1530) and
and displays the hours and minutes between the two times. This script has been
testing using a variety of patterns in addition to the patterns in the book (eg.,
2400 > 2330; 0720 > 1840; 2330 > 2300) which surfaced many errors (now fixed).
"""

print("\nEnter two different military time values (0530, 1750) to see the\n\
hours and minutes that elapse between them. \n")

MIDNIGHT = 1200 # using AM_PM time instead of military time for calculations
NOON = 1200
MINUTES_PER_HOUR = 60

print("=" * 60)

time_one = int(input("Please enter the first time:  "))
time_two = int(input("Please enter the second time: "))

# Regardless of whether time_one is greater than time_two (or vice versa), minutes
# for time_one are always subtracted from a full-hour increment and the difference is
# added to the time (counting up to NOON or MIDNIGHT, as the case may be). The
# last two digits of military time are minutes, so easy to get using modulus
# with 100 (% 100). Hours are basically the quotient of the time ( // 100). )

minutes_time_one = time_one % 100
if minutes_time_one > 0:
    minutes_time_one = MINUTES_PER_HOUR - minutes_time_one
minutes_time_two = time_two % 100
minutes = minutes_time_one + minutes_time_two

# Time one (time_one) is used to calculate hours until MIDNIGHT, and time_two
# captures hours from MIDNIGHT to the time specified.

if time_one > time_two:
    converted_time = (time_one-NOON) # assuming time is after NOON
    hours = (MIDNIGHT - (converted_time)) // 100
    hours = hours + (time_two // 100)

# Time_one starts calculation up until NOON and then adds time after NOON until
# the second time. Tested using various patterns (eg, 2300 and 2350, 50 minutes)
elif time_one < time_two:
    hours = ((NOON - time_one) // 100) + ((time_two - NOON) // 100)

if minutes >= MINUTES_PER_HOUR:
    hours += (minutes/MINUTES_PER_HOUR)
    minutes = abs(MINUTES_PER_HOUR - minutes)

print(int(hours), " hours ", minutes, " minutes")
