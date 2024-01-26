import random 

n = random.randint(1,20)

choice = int(input('Guess the number between 1 to 10: '))

attempts = 5

while attempts > 0:
    attempts -= 1
    if n == choice:
        print('Correct!')
    else:
        choice = int(input('Wrong! Try again: '))
