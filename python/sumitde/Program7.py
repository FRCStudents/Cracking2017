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
def remove():
    if len(x) >= 3:
        x.pop(2)
        print(x)
    else:
        print("Error: There is no third element!")

create()
cut()
remove()
