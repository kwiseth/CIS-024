#!/usr/bin/python3.6/time_elapsed_calculator.py

"""Exercise P2.17. Lets user enter two military time values (0730, 1530) and
and displays the hours and minutes between the two times.
"""

print("\nEnter two different military time values (0530, 1750) to see the\n \
hours and minutes that elapse between them. \n")

MIDNIGHT = 2400
NOON = 1200
MIDNIGHT_AM_PM = 1200
MINUTES_PER_HOUR = 60

print("=" * 60)

time_one = int(input("Please enter the first time:  "))
time_two = int(input("Please enter the second time: "))

# time_one starts calculation up until midnight and then adds time from midnight
# until time the following day. Tested using various patterns (eg, 2350 and 2300,
# resulting in 23 hours 10 minutes.

if time_one > time_two:
    hours = (MIDNIGHT_AM_PM - (time_one-NOON)) // 100
    minutes = (time_one-NOON) % 100
    hours = hours + (time_two // 100)
    minutes = minutes + (time_two % 100)

# time_one starts calculation up until noon and then adds time after noon until
# the second time. Tested using various patterns (eg, 2300 and 2350, 50 minutes)

elif time_one < time_two:
    hours = ((NOON - time_one) // 100) + ((time_two - NOON) // 100)
    # need to subtract for times prior to NOON this gives us just the minutes
    minutes = MINUTES_PER_HOUR - (time_one % 100) + (time_two % 100)

if minutes >= MINUTES_PER_HOUR:
    hours += minutes/MINUTES_PER_HOUR
    minutes = (minutes - MINUTES_PER_HOUR)

print(int(hours), " hours ", minutes, " minutes")
