import os

fruits = ['Apple','Orange','Banana','Watermelon','Pine Apple','Coconut']

result = ['Apple','Orange','Banana','Watermelon','Pine Apple','Coconut']

def Menu():
    os.system("cls")
    i = 0
    for option in fruits:
        i = i + 1
        print("{}. {}".format(i,option))



Menu()