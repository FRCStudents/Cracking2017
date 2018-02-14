def mult():
    c = []
    x = []
    print("Input anything!")
    x = input()
    print("Now, type a number!")
    z = int(input())
    for b in range(len(x)):
        v = ord(x[b])
        v = z + v
        c.append(chr(v))
    for b in range(len(x)):
        if b == 0:
            r = str(c[b])
        else:
            r = r + str(c[b])
    print(r)
mult()
