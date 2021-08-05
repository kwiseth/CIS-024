#!/usr/bin/python3.6/letter_grades.py

"""Exercise P3.12. User enters a letter grade at prompt and the script converts
to numeric value. Only VALID_INPUT entries are evaluated. The check for
letter_grade[0] != 'F' is not needed if F- and F+ are removed from VALID_INPUT.
"""

VALID_INPUT = {'A', 'A+', 'A-', 'B', 'B+', 'B-', 'C', 'C+', 'C-', 'D', 'D+',\
'D-', 'F', 'F-', 'F+'}

GRADE_POINTS = {'A' : 4.0, 'B' : 3.0, 'C' : 2.0, 'D' : 1.0, 'F' : 0}

letter_grade = input("Enter a letter grade: ").upper()

if not letter_grade in VALID_INPUT:
    exit("Please enter a valid letter grade, A thru F only (A, A+, A-, B, B+, ... F): ")

else:
    grade_pts = GRADE_POINTS[letter_grade[0]]
    if letter_grade.endswith("-") and letter_grade[0] != 'F':
        grade_pts = grade_pts - 0.3
    if letter_grade.endswith("+") and letter_grade[0] != 'A' and letter_grade[0] != 'F':
        grade_pts = grade_pts + 0.3
    print("The numeric value is", grade_pts)
