import random  
x = [0,0,0,0,0,0,0,0,0,0]
def create():
    for i in range(0,10):
        x[i] = random.randint(1,9)
    print(x)
def smush():
    for i in range(0,5):
        print(x[(2 * i)])
create()
smush()
