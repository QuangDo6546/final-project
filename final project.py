import os
import random
fruits = ['Apple','Orange','Banana','Watermelon','Pine Apple','Coconut']

result = ['Apple','Orange','Banana','Watermelon','Pine Apple','Coconut']

random.shuffle(result)

picker = []
player = []

picker.append(result[0])
picker.append(result[1])
picker.append(result[2])


def random_pick():
    list_result = []
    print("The result is: {}".format("".join(picker)))
    for item in player:
        for up in picker:
            if(item==up):
                list_result.append(up)
    if len(list_result)> 0:
        print("You won: {}".format(''.join(list_result)))
    else:
        print("Good luck next time! ")






def Menu():
    os.system("cls")
    i = 0
    for option in fruits:
        i = i + 1
        print("{}. {}".format(i,option))

        choice = int(input("Enter a number of fruits you want to choice: "))
        if (choice == 7):
            print("Thanks for playing.")
Menu()