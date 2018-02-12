import random
x = [0,0,0,0,0,0,0,0,0,0]
def create():
    for i in range(0,random.randint(1,9)):
        x[i] = random.randint(1,9)
def cut():
    if x[-1] == 0:
        x.pop()
        cut()
    else:
        print(x)

create()
cut()

y = input("By what exponent do you want to raise each element in the list? ")

def powArray(a,b):
    for i in range(0,len(a)):
        a[i] = (a[i] ** b)
    print(a)

powArray(x,y)
