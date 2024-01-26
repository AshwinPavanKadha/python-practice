
import random

player = input('Player Name:\t')
print(f"Hey {player}! Let's play Rock Paper Scisscors")

wins=0
losses=0
ties=0
while True:
    print(f'{wins} Wins, {losses} Losses, {ties} Ties') 

    while True:
        
        user_choice = input('Enter your move: \n\tRock: r\n\tPaper: p\n\tScissors:  s\n\tQuit:  q\n')

        if user_choice == 'r':
            print('ROCK versus ',end='')
            break
        elif user_choice == 'p':
            print('PAPER versus ',end='')
            break
        elif user_choice == 's':
            print('SCISSORS VERSUS ',end='')
            break
        elif user_choice =='q':
            exit()
        else:
            print('Wrong choice! Try again.')

    n=random.randint(1,3)

    if n == 1:
        comp_choice='r'
        print('ROCK')
    elif n==2:
        comp_choice='p'
        print('PAPER') 
    else:
        comp_choice='s'
        print('SCISSORS')


    if user_choice=='p' and comp_choice=='s':
        print('computer win and you lost')
        losses+=1
    elif user_choice=='p' and comp_choice=='r':
        print('computer lost and you win')
        wins+=1
    elif user_choice=='s' and comp_choice=='p':
        print('computer lost and you win')
        wins+=1
    elif user_choice=='s' and comp_choice=='r':
        print('computer win and you lost')
        losses+=1
    elif user_choice=='r' and comp_choice=='s':
        print('computer lost and you win')
        wins+=1
    elif user_choice=='r' and comp_choice=='p':
        print('computer win and you lost')
        losses+=1 
    else:
        print("It's a Tie!")
        ties+=1

    print('\n ---- END ---- \n\n')
