x = input("Enter a value you want for X ") 
y = input("Enter a value you want for y ")
arr = []
print("this is arr")
print(arr)
def add():
    arr.append(x)
    arr.append(y)
add()
print("this is arr after 1, and two are added to the list")
print(arr)
def remove():
    arr.pop(0)
print("this is arr after the first spot is removed")
remove()
print(arr)

