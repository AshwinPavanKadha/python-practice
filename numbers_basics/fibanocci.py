
# Write a Python Program to Print the Fibonacci sequence.

num = int(input("enter 'n' of terms to generate :\t"))
f0=0
f1=1
if num<0:
    print('enter number positive integer')
elif num == 0:
    print( f'fibanocci sequence upto {num} terms : ' )
    print(f0)
else:
    print('fibanocci sequence : ')

    for i in range(0,num):
        # f0=i
        print(f1)
        f2=f0+f1
        f0=f1
        f1=f2
        
