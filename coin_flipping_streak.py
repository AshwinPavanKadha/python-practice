

import random

streak = 0

for experiments in range(10000):
    coin_toss = []
    
    # 1) the first part generates a list of randomly selected 'heads' and 'tails' values
    for i in range(100):
        coin_toss += [random.choice(['H','T'])]

    #print(coin_toss)
    #print(len(coin_toss))

    # 2) the second part checks if there is a streak in it

    for j in range(94):
        if coin_toss[j:j+6] == ['H','H','H','H','H','H'] or coin_toss[j:j+6] == ['T','T','T','T','T','T']:
            streak += 1
            #print(coin_toss[j:j+6])

print(f'Percentage of streak of 6 is {streak/100/10000}%')
