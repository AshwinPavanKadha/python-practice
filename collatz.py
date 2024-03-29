'''#1) Collatz Sequence

Write a function named collatz() that has one parameter named number. 
If number is even, then collatz() should print number // 2 and return this value. 
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer 
and that keeps calling collatz() on that number until the function returns the value 1. 


The output of this program could look something like this:

Enter number:
3
10
5
16 
8 
4 
2 
1
'''

def collatz(num):
    if num%2==0:
        return (num//2)
        
    else:
        return ((3*num)+1)

n=int(input('Enter number: '))
while True:
    n=collatz(n)
    print(n)

    if n==1:
        break

