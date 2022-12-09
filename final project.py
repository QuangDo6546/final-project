
import random
fruits = ['Apple','Orange','Banana','Watermelon','Pine Apple','Coconut']

result = ['Apple','Orange','Banana','Watermelon','Pine Apple','Coconut']

random.shuffle(result)

picker = []
player = []

picker.append(result[0])
picker.append(result[1])
picker.append(result[2])


def conever_choice (index):
    return fruits [index]

list_result = []

def random_pick():
    
    print("The result is: {}".format(", ".join(picker)))
    for item in player:
        for up in picker:
            if(item==up):
                list_result.append(up)
    if len(list_result)> 0:
        print("You won: {}".format(', '.join(list_result)))
        print("Won fruits have been created to a text file at C: \ user \ your name \ fruits.txt")
    else:
        print("Good luck next time! ")


def txt_file():
    myFile = open("fruits.txt", "w")
    myFile.write("You won: ")
    i = 0
    for data in list_result:
        i = i + 1
        myFile.write("\n{}.{}".format(i,data))
   
    myFile.close()
    


def Menu():
    while True:
        print("1.Apple")
        print("2.Orange")
        print("3.Banana")
        print("4.Watermelon")
        print("5.Pine Apple")
        print("6.Coconut")
        print("7.Exit")
        

        choice = int(input("Enter a number of fruits you want to choice: "))
        if (choice == 7):
            print("Thanks for playing.")
            return True
        
        
        if (choice == 0):
            print("Invalid input, try again!")
            print()

        if (choice >=8):
            print("Invalid input, try again!")        
        else:
            player.append(conever_choice(int(choice)-1))
            return False

while True:
    
    if len(player)> 0:
            print()
            print()
            print("You choose: {}".format(', '.join(player)))
            continue_choice = input("Do you want to continue choice? (y/n) ")
            if continue_choice == 'y':
                if Menu():
                    break
            elif continue_choice == 'n':
                random_pick()
                txt_file()
                break
            else:
                print("Please enter invalid input!")
    else:
        if Menu():
            break
            

