import random
playing = True
number = str(random.randint(10,20))
print("i will generate number from 10 to 20 and u have to guess the number")
print("game ends when u get one hero!")
while playing:
    guess = input("give me ur best guess\n")
    if number== guess:
        print("u win the game")
        print("the number was",number)
        break
    else:
        print("ur guess is not right.try again. \n")
