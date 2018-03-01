a = 0
b = 0
c = 0
d = 0
x = 0
y = 0

def ask():
    a = input("How many steps up do you want to take?")
    b = input("How many steps down do you want to take?")
    c = input("How many steps left do you want to take?")
    d = input("How many steps right do you want to take?")
    global x
    global y
    x = x + d - c
    y = y + a - b
    game()

def game():
    global x
    global y
    if x >= 10:
        print("Let's keep you safe!")
        x = 10
    if y >= 10:
        print("Let's keep you safe!")
        y = 10
    if x <= -10:
        print("Let's keep you safe!")
        x = -10
    if y <= -10:
        print("Let's keep you safe!")
        y = -10
    if x >= 0 and y >= 0:
        print("Welcome to Colorado!")
        print("You should check out the mountains!")
    if x <= 0 and y >= 0:
        print("Welcome to Utah!")
        print("Go Mormons!")
    if x >= 0 and y <= 0:
        print("Welcome to New Mexico!")
        print("You should go to tbe UFO museum!")
    if x <= 0 and y <= 0:
        print("Welcome to Arizona!")
        print("You HAVE to see the Grand Canyon!")
    quit()

def quit():
    m = input("Do you want to keep going? If yes, type 1. If no, type some other number.")
    if m != 1:
        print("Come again!")
    if m == 1:
        ask()


ask()
