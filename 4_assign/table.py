##
#  This program prints a table of powers of x.
#

# Initialize constant variables for the max ranges.
#XMAX = 6
#NMAX = 3

"""# Print table header.
for n in range(1, NMAX + 1) :
   print("%10d" % n, end="")

print()
for n in range(1, NMAX + 1) :
   print("%10s" % "x ", end="")

print("\n", "    ", "-" * 35)
"""
"""
# Print table body.
for x in range(1, XMAX + 1) :
   # Print the x row in the table.
   for n in range(1, NMAX + 1) :
        print("%10.0f" % x ** n, end="")

   print()

"""
for i in range(10):
    for j in range(1, 4):
        print(i * j, end="")
    print()
