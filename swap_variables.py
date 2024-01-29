# Write a Python program to swap two variables.

var_1 = input('enter first variable : ')
var_2 = input('enter second variable : ')
print(f'given variables are {var_1} and {var_2}')
temp = var_2
var_2 = var_1
var_1 = temp
print(f'variables after swapping {var_1} and {var_2}')



# Write a Python program to swap two variables without temp variable.


var_1 = input('enter first variable : ')
var_2 = input("enter second variable : ")
print(f'variables brfore swapping : {var_1} and {var_2}')
var_1,var_2 = var_2,var_1

print(f'variables after swapping: {var_1} and {var_2}')
