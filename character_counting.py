'''
"Given message = 'This is python beginners course by techTFQ.'

Write a program that will count how many times each character is repeated in given message.

While displaying, use pprint.pprint(count) instead of print(count) [import pprint in the beginning]"
'''

source = input('enter a string:\t')

for i in source:
    num=source.count(i)
    if i==source[source.index(i)]:
        print(f'character "{i}" is repeated {num} times')
    else:
        break
