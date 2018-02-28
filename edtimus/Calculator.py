x = raw_input("What is your first number?")
y = raw_input("What is your second number?")
z = raw_input("Type 1 to add, 2 to subtract, 3 to multiply, 4 to divide")
a = 0

def solve():
    if int(z) == 1:
        a = int(x) + int(y)
    if int(z) == 2:
        a = int(x) - int(y)
    if int(z) == 3:
        a = int(x) * int(y)
    if int(z) == 4:
        a = int(x) / int(y)
    else:
        a = "undefined"
    print(a)

solve()

