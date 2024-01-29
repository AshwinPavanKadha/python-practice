# Write a Python Program to Add Two Matrices.


mat1=[[1,2,3],
   [4,5,6],
   [7,8,9]]

mat2=[[9,8,7],
   [6,5,4],
   [3,2,1]]
def matric_addition(x,y):
    if len(mat1) != len(mat2) or len(mat1[0])!=len(mat2[0]):
        print('Matrix size should be same for addition')
    add_matric = []
    result = []
    for i in range(0,len(mat1)):
        j=i
        add_matric.append(mat1[i][j]+mat2[i][j])
        result.append(add_matric)
    return result

sum=matric_addition(mat1,mat2)
print(sum)



