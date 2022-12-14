# final project.py
# Quang Anh Do
# 8776546
# PROG1783
# Date created: December 05, 2022
# Date Completed: December 10, 2022

#This program I will make a fruits choice game. This game is simply base on gourd crab shrimp fish game.
# You can find the information about the game here: 
# https://en.wikipedia.org/wiki/B%E1%BA%A7u_cua_t%C3%B4m_c%C3%A1#:~:text=B%E1%BA%A7u%20cua%20t%C3%B4m%20c%C3%A1%20(%20lit,T%E1%BA%BFt%20(Vietnamese%20New%20Year).
# Rule: The program will print 6 different fruits to the console and ask user which fruits they want to choose by type a number.
# The program will continue to ask user if they want to choose more fruits or no
# After that, the program will random pick 3 diffrent fruits for the result, if the fruits match any user choice fruits
# The program will print the result and the fruits match with the result to the console,also the program will write the fruits match to a text file
# If nothing match the result, the program will print good luck next time.


#Import random module to random the result.
import random
# 2 lists of fruits
fruits = ['Apple','Orange','Banana','Watermelon','Pine Apple','Coconut']

result = ['Apple','Orange','Banana','Watermelon','Pine Apple','Coconut']

random.shuffle(result)          #Random the list above 

# create 2 empty list to store the result
picker = []
player = []

#Append 3 different fruits to result
picker.append(result[0])
picker.append(result[1])
picker.append(result[2])


#Function to return the fruits list
def conever_choice (index):
    return fruits [index]

#Another wmpty list to store user input
list_result = []

# Function to print the result
def random_pick():
    print("The result is: {}".format(", ".join(picker)))    #Print the results
    for item in player:
        for up in picker:
            if(item==up):
                list_result.append(up)      #Match the user input to result
    #If user choice match any result, the program will print the fruits match, if not the program will print good luck next time
    if len(list_result)> 0:
        print("You won: {}".format(', '.join(list_result)))
        print("Won fruits have been created to a text file at C: \ user \ your name \ fruits.txt")      #Print the message the fruits have been created to a text file
    else:
        print("Good luck next time! ")

#Function to write the file
def txt_file():
    myFile = open("fruits.txt", "w")    #open the file as write mode
    myFile.write("You won: ")
    i = 0
    for data in list_result:            #Mke the list with number for every won fruits
        i = i + 1
        myFile.write("\n{}.{}".format(i,data))
   
    myFile.close()                      #Close the file
    
#Function to display the list of fruits
def Menu():
    #Loop the list until the user does't want to choose anymore fruit
    while True:
        print("1.Apple")
        print("2.Orange")
        print("3.Banana")
        print("4.Watermelon")
        print("5.Pine Apple")
        print("6.Coconut")
        print("7.Exit")
        
        #Ask user enter a number of the fruits
        choice = int(input("Enter a number of fruits you want to choice: "))
        if (choice == 7):                       #If user type 7, the program will stop and display a message thanks for playing
            print("Thanks for playing.")
            return True
        
        if (choice == 0):                       #If user type 0, the program will print the message ask user type other number
            print("Invalid input, try again!")
            print()

        if (choice >=8):                        #Same as > = 8
            print("Invalid input, try again!")        
        else:
            player.append(conever_choice(int(choice)-1))
            return False

#Loop the input ask user if they want to choose more fruit or no, if not the program will stop and display the result
while True:
    if len(player)> 0:
            print()
            print()
            print("You choose: {}".format(', '.join(player)))                 #Print the fruits user choose
            continue_choice = input("Do you want to continue choice? (y/n) ") #Ask user if they want to choose more fruits
            if continue_choice == 'y':                                         #If yes, the program will continue to display the menu
                if Menu():
                    break
            elif continue_choice == 'n':                                       #If not, the program will stop and display the result
                random_pick()
                txt_file()                                                      #Call write function
                break
            else:                                                   
                print("Please enter invalid input!")                            #If user type other than y/n, the program will continue to ask until they type y/n
    else:
        if Menu():
            break
            

