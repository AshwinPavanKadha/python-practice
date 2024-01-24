"""
Write a Python Program to Display Fibonacci Sequence Using Recursion.
Fibonacci sequence:
The Fibonacci sequence is a series of numbers in which each number is the sum of the two
preceding ones, usually starting with 0 and 1. In mathematical terms, it is defined by the
recurrence relation ( F(n) = F(n-1) + F(n-2) ), with initial conditions ( F(0) = 0 ) and ( F(1) = 1
). The sequence begins: 0, 1, 1, 2, 3, 5, 8, 13, 21, and so on. The Fibonacci sequence has
widespread applications in mathematics, computer science, nature, and art.
"""


def feb(n):
    if n<=1:
        return n
    else:

        return (feb(n-1)+feb(n-2))

nterms = int(input('enter no of terms : \t'))

if nterms<=0:
    print('enter positive number ')
else:
    print('Fibannoci Sequence:')
    for i in range(nterms):
        print(feb(i))



"""
# Python program to display the Fibonacci sequence
def recur_fibo(n):
    if n <= 1:
        return n
    else:
        return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = int(input("Enter the number of terms (greater than 0): "))
# check if the number of terms is valid
if nterms <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
for i in range(nterms):
    print(recur_fibo(i))
"""







'''
def fact(a):
if n==1 :
    return n
else: 
    return (a*fact(a-1))
n = int(input('enter number : \t'))
if num<0 :
    print('Sorry, factorial does not exits for negative numbers)
elif n == 0:
    print('factorail is 1')
else:
    print(f'factorial of {n} is {fact(n)}')
'''





"""
# Factorial of a number using recursion
def recur_factorial(n):
    if n == 1:
        return n
    else:
        return n*recur_factorial(n-1)
num = int(input("Enter the number: "))
# check if the number is negative
if num < 0:
    print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    print("The factorial of", num, "is", recur_factorial(num))
"""

