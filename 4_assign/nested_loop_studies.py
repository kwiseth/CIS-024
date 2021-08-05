>>> for i in range(3):
...     for j in range(5) :
...         print(i, "\t", j)
... 
0 	 0
0 	 1
0 	 2
0 	 3
0 	 4
1 	 0
1 	 1
1 	 2
1 	 3
1 	 4
2 	 0
2 	 1
2 	 2
2 	 3
2 	 4



# Python Program to Print Hollow Square Star Pattern

side = int(input("Please Enter any Side of a Square  : "))

print("Hollow Square Star Pattern") 
for i in range(side):
    for j in range(side):
        if(i == 0 or i == side - 1 or j == 0 or j == side - 1):
            print('*', end = '  ')
        else:
            print(' ', end = '  ')
    print()
