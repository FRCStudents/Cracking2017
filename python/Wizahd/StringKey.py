def mult():
    c = []
    x = []
    print("Input anything!")
    x = input()
    print("Now, type a number!")
    z = int(input())
    if z == 0:
        print("That doesn't do anything!")
    else:
        for b in range(len(x)):
            v = ord(x[b])
            v = z + v
            if ord("z") > v > ord("a") or ord("Z") > v > ord("A"):
                h = 0
            else:
                if v > ord("z"):
                    v = ord("a") + (z-1)
                else:
                    v = ord("A") + (z-1)
            c.append(chr(v)) 
        for b in range(len(x)):
            if b == 0:
                r = str(c[b])
            else:
                r = str(r + c[b])
        print(r)
mult()
