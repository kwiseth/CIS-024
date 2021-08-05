#!/usr/bin/python3.6/time_elapsed_calculator_alt.py

"""Exercise P2.17.(alternate) Lets user enter two military time values (0730, 1530) and
and displays the hours and minutes between the two times.
"""

print("\nEnter two different military time values (0530, 1750) to see the\n \
hours and minutes that elapse between them. \n")

MIDNIGHT = 1160
NOON = 1160
MINUTES_PER_HOUR = 60

print("=" * 60)

time_one = int(input("Please enter the first time:  "))
time_two = int(input("Please enter the second time: "))


if time_one > time_two:
    # first two calculations give us time elapsed between time_one and midnight
    hours = MIDNIGHT - time_one
    print(hours)
    minutes = (time_one-NOON) % 100
    print(minutes)
    hours = hours + (time_two // 100)
    print(hours)
    minutes = minutes + (time_two % 100)
    print(minutes)

elif time_one < time_two:
    hours =  ((NOON - time_one) // 100) + ((time_two - NOON) // 100)
    minutes = MINUTES_PER_HOUR - (time_one % 100) + (time_two % 100) # need to subtract for times prior to NOON this gives us just the minutes

if minutes >= MINUTES_PER_HOUR:
    hours += minutes/MINUTES_PER_HOUR
    minutes = (minutes - MINUTES_PER_HOUR)

print(int(hours), " hours ", minutes, " minutes" )
