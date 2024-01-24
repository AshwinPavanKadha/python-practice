# Write a Python program to do arithmetical operations addition and division.

"""
num1= float(input('enter number first number : \n'))
num2= float(input('enter number second number : \n'))

sum_result = num1 + num2
print(f' sum of {num1} and {num2} = {sum_result}')

division_result = num1 / num2
print(f' division of {num1} / {num2} = {division_result}')

"""

# Write a Python program to find the area of a triangle.

"""
base  = float(input('enter base of traingle : '))
height = float(input('enter height side of triangle : '))

area = 0.5 * base * height
print(f'area of traingle : {area}')
"""



# Write a Python program to generate a random number.

"""
import random
print(f' the random number is {random.randint(1,100)}')
"""


# Write a Python program to convert kilometers to miles.

"""
kilometer = float(input ('enter distance in kilometers =\t'))
miles = kilometer*1.6
print(f' Distance in miles = {miles}')
"""

# Write a Python program to convert Celsius to Fahrenheit.

"""
celsius = float(input('enter temperature in celsius = \t'))
farenheit = ((9/5) * celsius) + 32
print(f'temperature in farenheit = {farenheit}')
"""



# Write a Python program to display calendar.

'''
import calendar

year = int(input('enter year : \t'))
month = int(input('enter month : \t'))

cal = calendar.month(year,month)
print(cal)
'''


# Write a Python program to solve quadratic equation.

# (-b+_ ((b^2) - 4 * a * c)^0.5)/(2*a)
"""
import math
a = float(input('enter cofficient a = '))
b = float(input('enter cofficient b = '))
c = float(input('enter cofficient c = '))

discriminant = (b**2) - 4 * a * c

if discriminant > 0 :
    root1 = ((-b) + discriminant)/(2*a)
    root2 = ((-b) - discriminant)/(2*a)
    print(f"Root 1 = {root1}")
    print(f'Root 2 = {root2}')
elif discriminant == 0:
    root = (-b)/(2*a)
    print(f'Root = {root} ')
else : 
    real = -b/(2*a)
    imaginary = math.sqrt(abs(discriminant))/(2*a)
    print(f'Root1 = {real} + {imaginary}i')
    print(f'Root2 = {real} - {imaginary}i')
"""


# Write a Python Program to Check if a Number is Positive, Negative or Zero.

"""
num = float(input('enter the number to guess: \t'))
if num == 0 :
    print(f'given number {num} is not positive nor negative ')
elif num > 0:
    print(f'given number {num} is positive')
else:
    print(f'given number {num} is negative')
"""



# Write a Python Program to Check if a Number is Odd or Even.

"""
num = int(input('enter numbner to guess : '))

if num == 0 :
    print(f'enter number other than 0') 
elif num%2 == 0 :
    print(f'given number {num} is even ')
else :
    print(f'given number {num} is odd')
"""



# Write a Python Program to Check Leap Year.

'''
year = int(input('enter year to check it is leap or not :'))
if year%400 == 0 and year%100 == 0:
    print(f'{year} is leap year')
elif year%4==0 and year%100!=0 :
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
'''



# Write a Python Program to Check Prime Number.

"""
flag = False
num = int(input('enter number to check : \t'))
if num == 1 :
    print(f'{num} is nor prime nor composite' )

for i in range(2,num):
    if num % i ==0:
        print(f'{num} is composite')
        flag = True
        break

if flag:
    print(f'{num} is not prime')
else:
    print(f'{num} is a prime')
"""




# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.

"""
lower = 2
upper = 10
for i in range(lower, upper+1):
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            print(i)
"""



# Write a Python Program to Find the Factorial of a Number.

'''
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
'''


# Write a Python Program to Display the multiplication Table.

'''
j = int(input('enter nth table: \t'))
for i in range(1,11):
    print(f'{i} x {j} = {i*j}')
'''







# Write a Python Program to Find the Sum of Natural Numbers.

'''
n = int(input('enter sum of first n natural numbers : '))
sum = 0 
for i in range(1, n+1):
    sum+=i
print(sum)
'''



# Write a Python Program to Find LCM.

'''
def compute_lcm(x,y):
    if n1> n2 :
        greater = n1
    else :
        greater = n2
    while True:
        if (greater%n1) == 0 and (greater%n2) == 0:
            lcm = greater
            break
        greater+=1
    return lcm


n1 = int(input('enter first number : '))
n2 = int(input('enter second number : '))
print(f'lcm of {n1} and {n2} is compute_lcm(n1,n2)')
'''



# Write a Python Program to Find HCF.


'''
n1 = int(input('enter first number : '))
n2 = int(input('enter second number : '))
hcf = 1
if n1<n2:
    i=n1
else:
    i=n2
for i in range(2,i+1):
    if n1%i == 0 and n2%i==0 :
        hcf = i
print(f'HCF of {n1} and {n2} is {hcf}')
'''

# Write a Python Program to Make a Simple Calculator with 4 basic mathematical operations.


"""
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
"""


# Write a Python Program to calculate your Body Mass Index.

"""
weight = int(input('enter weight in kgs: '))
height = float(input('enter height in inch: '))
def bodymassindex(w, h ):
    return (round(w/((h**2)),2))
bmi = bodymassindex(weight, height)
print(bmi)

if bmi<=18.5:
    print('under weight')
elif 18.5< bmi <=24.9:
    print('normal weight')
elif 25 < bmi< 29.29 :
    print('overweight weight')
else :
    print('You are obesse')
"""


# Write a Python Program to calculate the natural logarithm of any number.

"""
import math

num = float(input('enter a number :'))
if num <= 0:
    float(input('enter positive number :'))
else :
    result = math.log(num)
    print(f' The natural logarithm of {num} is {result}')
"""



# Write a Python Program for cube sum of first n natural numbers?

'''
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
'''






