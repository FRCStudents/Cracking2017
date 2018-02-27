import random

x = [0,0,0,0,0]
         
def create():
    for i in range(0,5):
        x[i] = random.randint(1,9)
                                                                                                                                                                       
def cut():
    if x[-1] == 0:
        x.pop()
        cut()
    else:
        print(x)

def distribute():
    for i in range(0,len(x)):
        print(x[i])

create()                                        
cut()
distribute()
