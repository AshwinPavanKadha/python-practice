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
        print(f'{num//2}')
        return num//2
    if num%2!=0:
        print((3*num)+1)
        return (3*num)+1
numb=int(input('enter number:'))
test=0
while test!=1:
    test=collatz(numb)
    if test%2==0:
        print(f'{test//2}')
    if test%2!=0:
        print((3*test)+1)
        

