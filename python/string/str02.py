
#############################################
# here is some stuff you can do with strings #
# in python                                  #
##############################################

s1 = "This is a string like nobody's business"
print("STRING: " + s1)
print("\tLOWER: " + s1.lower())
print("\tUPPER: " + s1.upper())
print("Count 'i': ", s1.count('i'))
print("Count 'T': ", s1.count('T'))
print("Count 'T' or 't': ", s1.upper().count('T'))

print("And some other functions, like find...")
print("Find 'nobody': ",  s1.find("nobody"))
print("Replace 'nobody' with 'somebody': " + s1.replace("nobody", "somebody"))


print("You can also get pieces of strings: ")
print(s1[5:7])
print("That " + s1[5:])
print(s1[0:-8] + "STUFF")

print("Length: ", len(s1))
print("Every other char: " + s1[0::2])
print("Every third char: " + s1[0::3])
print("And backwords: " + s1[::-1])
