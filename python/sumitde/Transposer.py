def transpose():
    string = raw_input("What string do you want to transpose:")
    key = input("What key do you want to transpose with:")
    letters = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    otherletters = ["a","b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    otherstring = list(string.lower()) 
    for i in range(0,key):
        x = letters[0]
        letters.pop(0)
        letters.append(x)
    for i in range(0,len(otherstring)):
        for j in range(0,len(otherletters)):
            if otherstring[i] == otherletters[j]:
                otherstring[i] = letters[j]
                break            
    string = "".join(otherstring)
    print(string)                
    again()   

def again():
    response = input("Do you want to transpose another string? (Type 1 if yes, 2 if no)")
    if response == 1:
        transpose()
    if response == 2:
        print("OK!")


transpose()
