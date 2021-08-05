# nested_loops.py

side = int(input("input the side dimension of the square: "))

for i in range(side) :
    for j in range(side * 2 + 1) :
        print(i, "\t", j)
