
# Write a Python Program to Find the Sum of Natural Numbers.


n = int(input('enter sum of first n natural numbers : '))
sum = 0 
for i in range(1, n+1):
    sum+=i
print(sum)


# Write a Python Program for cube sum of first n natural numbers?


def cubesum(num):
    summing = 0
    if num<=0:
        print('enter positive number')
    else : 
        for i in range(1,num+1):
            summing += i**3
    return summing
a = int(input('enter a number of digits to sum :'))
if a<=0:
    print('please enter positive number ')
else :
    sum=cubesum(a)
    print(f'the cube sum of first {a} natural numbers is {sum}')
