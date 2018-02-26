import random
x = [0,0,0,0,0,0,0,0,0,0]
y = input("The number I want to insert is: ")
def create():
    for i in range(0,random.randint(1,9)):
        x[i] = random.randint(1,9)
def cut():
    if x[-1] == 0:
        x.pop()
        cut()
    else:
        print(x)
def splice():
    x.insert(1,y)
    print(x)

create()
cut()
splice()
