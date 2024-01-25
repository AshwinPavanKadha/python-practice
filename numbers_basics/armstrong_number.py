
# Write a Python Program to Check Armstrong Number?

num = input('enter number to check armstrong :')

power = len(num)

result = 0

for i in num:
    
    result+=int(i)**power

print(result)
if int(num) == result:
    print(f'{num} is armstrong number')
else:
    print('given number is not armstrong number')
