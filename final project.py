
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


def random_pick():
    list_result = []
    print("The result is: {}".format(" ".join(picker)))
    for item in player:
        for up in picker:
            if(item==up):
                list_result.append(up)
    if len(list_result)> 0:
        print("You won: {}".format('-'.join(list_result)))
    else:
        print("Good luck next time! ")






def Menu():
    
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
        
    else:
        player.append(conever_choice(int(choice)-1))
        return False

while True:
    
    if len(player)> 0:
            print()
            print("You choose: {}".format(', '.join(player)))
            continue_choice = input("Do you want to continue choice? (y/n) ")
            if continue_choice == 'y':
                if Menu():
                    break
            elif continue_choice == 'n':
                random_pick()
                break
            else:
                print("Please enter invalid input!")
    else:
        if Menu():
            break
            

