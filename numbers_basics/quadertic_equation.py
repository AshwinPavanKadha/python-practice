# Write a Python program to solve quadratic equation.

# (-b+_ ((b^2) - 4 * a * c)^0.5)/(2*a)

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

