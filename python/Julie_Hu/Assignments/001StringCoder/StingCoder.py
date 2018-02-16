plainText = input("What is the text you want to code? ")
key = int(input("What is your key? "))
def ar(plainText, key): 
    cipherText = "" 
    for x in plainText:
        if x.isalpha():
            stayInAlphabet = ord(x) + key 
        if stayInAlphabet > ord('z'):
            stayInAlphabet -= 26
            finalLetter = chr(stayInAlphabet)
            cipherText += finalLetter
    print("Your ciphertext is: ", cipherText)
    return cipherText

