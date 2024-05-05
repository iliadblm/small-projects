import random


def dice_roll():
    return random.randint(1, 6)


# print(dice_roll())

print("What's up! Now you\'re going to play one board game, let\'s get started")
print(input("[Enter to continue]"))

name1 = input("Enter your name, first player:   ")
name2 = input("Enter your name, second player:   ")

finish = False
square = 0
square2 = 0
win1 = False
win2 = False
while not finish:
    print("Let\'s start with the first player...")
    print(name1.upper(), ",Roll dice, please!")
    print(input("[Enter to roll dice]"))
    points = dice_roll()
    print("You\'ve got", points, "!")
    print(input("[Enter to continue]"))
    square = points + square
    print("You\'re on square number", square, "!")
    if square == 3:
        square -= 2
        print("What a pity...", name1, "have been rolled back to 2 cells(")
        print("Now", name1, "is on the cell number", square, "...")
    elif square == 5:
        square += 5
        print("Hooray!", name1, "have been moved 5 cells forward!")
        print("Now", name1, "is on the cell number", square, "!")
    elif square == 7:
        square -= 5
        print("What a pity...", name1, "have been rolled back to 5 cells(")
        print("Now", name1, "is on the cell number", square, "...")
    elif square == 11:
        square += 1
        print("Hooray!", name1, "have been moved 1 cell forward!")
        print("Now", name1, "is on the cell number", square, "!")
    elif square == 14:
        square -= 13
        print("GOD DAMN, WHAT A LOSEEEEEEER XD,", name1, "have been moved to the cell number 1 >:>")
        print("Now", name1, "is on the cell number", square, "...")
    elif square >= 15:
        finish = True
        win1 = True

    if not win1:
        print("Now the second player...")
        print(name2.upper(), ",Roll dice, please!")
        print(input("[Enter to roll dice]"))
        points2 = dice_roll()
        print("You\'ve got", points2, "!")
        print(input("[Enter to continue]"))
        square2 = points2 + square2
        print("You\'re on square number", square2, "!")
        if square2 == 3:
            square2 -= 2
            print("What a pity...", name2, "have been rolled back to 2 cells(")
            print("Now", name2, "is on the cell number", square2, "...")
        elif square2 == 5:
            square2 += 5
            print("Hooray!", name2, "have been moved 5 cells forward!")
            print("Now", name2, "is on the cell number", square2, "!")
        elif square2 == 7:
            square2 -= 5
            print("What a pity...", name2, "have been rolled back to 5 cells(")
            print("Now", name2, "is on the cell number", square2, "...")
        elif square2 == 11:
            square2 += 1
            print("Hooray!", name2, "have been moved 1 cell forward!")
            print("Now", name2, "is on the cell number", square2, "!")
        elif square2 == 14:
            square2 -= 13
            print("GOD DAMN, WHAT A LOSEEEEEEER XD,", name2, "have been moved to the cell number 1 >:>")
            print("Now", name2, "is on the cell number", square2, "...")
        elif square2 >= 15:
            finish = True
            win2 = True


if win1:
    print("HOORAAAAAAY,", name1.upper(), "WON THE GAME!!!")
elif win2:
    print("HOORAAAAAAY,", name2.upper(), "WON THE GAME!!!")
