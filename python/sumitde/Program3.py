import random
x = [0,0,0,0,0,0,0,0,0,0]
y = [0,0,0,0,0,0,0,0,0,0]
def create():
    for i in range(0,random.randint(1,9)):
        x[i] = random.randint(1,9)
def cut():
    if x[-1] == 0:
        x.pop()
        cut()
    else:
        print(x)
def reverse():
    for i in range(0,len(x)):
        y[i] = x[-1-i]
def cutreverse():
    if y[-1] == 0:
        y.pop()
        cutreverse()
    else:
        print(y)
create()
cut()
reverse()
cutreverse()
