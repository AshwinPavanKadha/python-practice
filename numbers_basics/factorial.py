# Write a Python Program to Find the Factorial of a Number.


num = int(input('enter a number to find factorail: '))
factorail = 1
if num<1:
    print('no factorial if number is neagative')
if num == 0 :
    print('factorail {num} is 1 ')
else:
    for i in range(2,num+1):
        factorail=factorail*(i)
    print(factorail)


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
