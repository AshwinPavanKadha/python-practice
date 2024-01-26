'''
Modify the above program such that every time the user gives a wrong answer, 
you provide tthe user with a hint saying if the choice was too low or too high.
'''


import random 

n = random.randint(1,10)

choice = int(input('Guess the number between 1 to 10: '))

attempts = 4

while attempts > 0:
    attempts -= 1
    if n == choice:
        print('Correct!')
        break
    
    if n>choice:
        choice = int(input('Wrong!, greater than guessed number. Try again: '))
        
    if n<choice:
        choice = int(input('Wrong!, less than guessed number. Try again: '))
