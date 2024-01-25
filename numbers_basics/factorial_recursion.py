# Write a Python Program to Find Factorial of Number Using Recursion.

def factorial(n):

    if n==1:
        return n
    else:
        return n*factorial(n-1)

num = int(input('enter number to find factorial : '))



if num<0:
    print('negative numbers deos not factorials')
elif num ==0 :
    print(f'factorail of {num} is 1')
else:
    print(f'factorial of {num} is {factorial(num)}')



