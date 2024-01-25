# Write a Python Program to Check Prime Number.


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





# Write a Python Program to Print all Prime Numbers in an Interval of 1-10.


lower = 2
upper = 10
for i in range(lower, upper+1):
    for j in range(2,i):
        if i%j == 0:
            break
        else:
            print(i)

