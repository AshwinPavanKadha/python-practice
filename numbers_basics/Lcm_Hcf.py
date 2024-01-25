# Write a Python Program to Find LCM.


def compute_lcm(x,y):
    if n1> n2 :
        greater = n1
    else :
        greater = n2
    while True:
        if (greater%n1) == 0 and (greater%n2) == 0:
            lcm = greater
            break
        greater+=1
    return lcm


n1 = int(input('enter first number : '))
n2 = int(input('enter second number : '))
print(f'lcm of {n1} and {n2} is compute_lcm(n1,n2)')




# Write a Python Program to Find HCF.



n1 = int(input('enter first number : '))
n2 = int(input('enter second number : '))
hcf = 1
if n1<n2:
    i=n1
else:
    i=n2
for i in range(2,i+1):
    if n1%i == 0 and n2%i==0 :
        hcf = i
print(f'HCF of {n1} and {n2} is {hcf}')
