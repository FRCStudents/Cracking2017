y = input("What number do you want to add:")
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
x.append(y)
print(x)

