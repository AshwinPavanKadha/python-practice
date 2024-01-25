# Write a Python Program to Check Leap Year.


year = int(input('enter year to check it is leap or not :'))
if year%400 == 0 and year%100 == 0:
    print(f'{year} is leap year')
elif year%4==0 and year%100!=0 :
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')



# Write a Python program to display calendar.


import calendar

year = int(input('enter year : \t'))
month = int(input('enter month : \t'))

cal = calendar.month(year,month)
print(cal)
