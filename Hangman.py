import random

field = ['hydrogen', 'helium', 'lithium','beryllium','boron', 'carbon', 'nitrogen','oxygen','fluorine','neon','sodium','magnesium','aluminum','silicon','phosphorus','sulfur','chlorine','argon']
strikes = 0
word = field[random.randint(0, 17)]
puzzle = list(word)
guesses = list(word)
for i in range(0,len(guesses)):
    guesses[i] = "_"
def game():
    print(" ".join(guesses))
    x = raw_input("Guess a letter:")
    global strikes
    strikes+=1
    y = 0
    for i in range(0,len(puzzle)):
        if x == puzzle[i]:
            guesses[i] = x
            y+=1
    if y >= 1:
        strikes-=1
    print("You now have %d strikes") % (strikes)
    if puzzle == guesses:
        print("Congratulations! You have solved the puzzle!")
    elif strikes == 3:
        print("3 strikes, you're out! Try again next time")
        print("The word was %s") % (word)
    else:
        game()

print("Welcome to hangman. The word is one of the first 18 elements in the periodic table. If you get three strikes, you're out. Guess away!")
game()



