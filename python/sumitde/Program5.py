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

y = [0,0,0,0,0,0,0,0,0,0] 
def recreate():
    for i in range(0,random.randint(1,9)):    
        y[i] = random.randint(1,9)
def recut(): 
    if y[-1] == 0:
        y.pop()
        recut()
    else:
        print(y)

create()
cut()
recreate()
recut()

def combine():
    for i in range(0,len(y)):
        x.append(y[i])
    print(x)

combine()

