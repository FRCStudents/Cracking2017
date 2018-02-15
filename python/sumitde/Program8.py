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

y = input("I want to remove the first occurence of this number from the list: ")

def count():
    for i in range(0, len(x)):
        if  y == x[i]:
            x.pop(i)
            break
    print(x)

create()
cut()
count()
    
            


