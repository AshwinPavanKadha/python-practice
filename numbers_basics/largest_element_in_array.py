# Write a Python Program to find largest element in an array.


largest = 0
my_list = [1,56,7,90,34,65]
for i in my_list:
    if i > largest:
        largest=i
print(largest)
