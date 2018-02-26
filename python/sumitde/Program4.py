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
a = input("Type a number: ")
def count():
    y = 0
    for i in range(0,len(x)):
        if a == x[i]:
            y += 1
    print("Your number appears %d times") % (y)
count()
