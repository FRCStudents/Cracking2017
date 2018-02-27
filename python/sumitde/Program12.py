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
def plusOne(a):
    for i in range(0,len(a)):
        a[i] = a[i] + 1
    print(a)

create()
cut()
plusOne(x)
