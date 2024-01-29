
# Write a Python Program to Multiply Two Matrices.


a=[[1,2,3],
   [4,5,6],
   [7,8,9]]

b=[[9,8,7],
   [6,5,4],
   [3,2,1]]



result = [[0,0,0],
         [0,0,0],
         [0,0,0]]

def matrix_multi(x,y):
    if len(a[0])!=len(b[0]):
        print('Matrix size should be same for multiplication')
    else:
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(result)):
                    result[i][j] += a[i][k]*b[j][k]
        return result
multiplication = matrix_multi(a,b)

print(f'Result of matrix multiplication :')
for row in result:
    print(row)  

