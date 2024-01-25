# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.



def sum(x,y):
    return x+y

def multiply(x,y):
    return x*y

def divide(x,y):
    return x/y

def subtract(x,y):
    return x-y

a = int(input('enter first number : \t'))
b = int(input('enter second number : \t'))
c = input('''enter your chpice 'p' for addition 
             enter your chpice 'q' for multiplication
             enter your chpice 'r' for division 
             enter your chpice 's' for subtractiob \n''')
if c == 'p':
    print(sum(a,b))
elif c == 'q':
    print(multiply(a,b))
elif c == 'r':
    print(divide(a,b))
elif c == 's':
    print(subtract(a,b))
else:
    c = input('enter valid choice :')
