'''Q40
"Write a program which request user to enter their email id and the program will then slice the username and domain and dislay them seperately.

For example, if email given is techtfq@gmail.com

the program should print as follows:
Username: techtfq
Domain: gmail.com"
'''


email=input('enter the mail:')


print(email.index('@'))

username = email[:email.index('@')]
domain = email[email.index('@')+1:]

print(f'Username is {username}')
print(f'Domain is {domain}')


print(f"Username is {email.split('@')[0]}")
print(f"Domain is {email.split('@')[1]}")

