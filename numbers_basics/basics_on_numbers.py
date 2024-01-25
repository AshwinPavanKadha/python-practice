# Write a Python program to do arithmetical operations addition and division.


num1= float(input('enter number first number : \n'))
num2= float(input('enter number second number : \n'))

sum_result = num1 + num2
print(f' sum of {num1} and {num2} = {sum_result}')

division_result = num1 / num2
print(f' division of {num1} / {num2} = {division_result}')



# Write a Python program to find the area of a triangle.


base  = float(input('enter base of traingle : '))
height = float(input('enter height side of triangle : '))

area = 0.5 * base * height
print(f'area of traingle : {area}')




# Write a Python program to generate a random number.


import random
print(f' the random number is {random.randint(1,100)}')



# Write a Python program to convert kilometers to miles.


kilometer = float(input ('enter distance in kilometers =\t'))
miles = kilometer*1.6
print(f' Distance in miles = {miles}')


# Write a Python program to convert Celsius to Fahrenheit.


celsius = float(input('enter temperature in celsius = \t'))
farenheit = ((9/5) * celsius) + 32
print(f'temperature in farenheit = {farenheit}')









# Write a Python Program to Check if a Number is Positive, Negative or Zero.


num = float(input('enter the number to guess: \t'))
if num == 0 :
    print(f'given number {num} is not positive nor negative ')
elif num > 0:
    print(f'given number {num} is positive')
else:
    print(f'given number {num} is negative')




# Write a Python Program to Check if a Number is Odd or Even.


num = int(input('enter numbner to guess : '))

if num == 0 :
    print(f'enter number other than 0') 
elif num%2 == 0 :
    print(f'given number {num} is even ')
else :
    print(f'given number {num} is odd')




















