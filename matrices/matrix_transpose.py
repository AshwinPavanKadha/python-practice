# Write a Python Program to Transpose a Matrix

a = [[1,2,3],
     [4,5,6],
     [7,8,9]]

rows , cols = len(a), len(a[0])

transpose = [[0 for _ in range(rows)] for _ in range(cols)]


for i in range(len(a)):
    for j in range(len(a[0])):
        transpose[j][i] = a[i][j]
for r in transpose:
    print(transpose)

