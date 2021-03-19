"""
Program Goals:
Do the things
"""

#create functions that will perform those actions above
myList = []
import random
CountList = []

print("Hello, there! Lets work with some lists today")

def mainProgram():
    while True:
        print("Choose one of the following options. Type a number ONLY")
        choice = input("""1. Add to List,
2. Add a bunch of Numbers
3. Return the value at an index prosition.
4. Get a random value that you have inputted.
5. Find where a number is in your list
6. Find out how many of one numbers are on your list
7. Clear your list and start again
8.Print your list
9. Quit the progam.    """)
        if choice == "1":
            addToList()
        elif choice == "2":
            addABunch()
        elif choice == "3":
            indexValues()
        elif choice == "4":
            randomSearch()
        elif choice == "5":
            linearSearch()
        elif choice == "6":
            howMany()
        elif choice == "7":
            myList.clear()
            print("You are all set")
        elif choice  == "8":
            print("Okay, {}".format(myList))
        elif choice =="9":
            print(""" Okay Bye ^-^
  (\_/)
  (^_^)
 (____)0""")
            break
        else:
            print("Im sorry that wast an option, try again please. Remeber that you can only use 1,2,3,4")
            mainProgram()
        print("""






*＊✿❀ ₍ᐢ ̥ ̞ ̥ᐢ₎ ♥ *＊✿❀
""")

def addToList():
    while True:
        print("Awesome what number do you want to add?     ")
        number = input("Please only write numbers like above! ^-^      ")
        try:
            if int(number)>0:
                print("great I'll add it to the list")
                myList.append(int(number))
                print(myList)
            else:
                print("Im sorry We can only do numbers above 0, do you wanna try again?")
                try1 = input(" ")
                if try1 == "yes":
                    print("Okay")
                    addToList()
                else:
                    print("Okay")
        except ValueError:
            print("Im sorry you have to use numbers, please try again")
            addToList()
        print("Do you want to continue")
        yesno = input ("Y or N   ")
        if yesno == "Y":
            print("Okay")
        elif yesno == "y":
            print("Great")
        else:
            break


def addABunch():
    print("Here we can add a bunch of numbers to the list")
    numToAdd = input("How many numbers do you want to add?    ")
    numRange = input("How high do you want the numbers to go?   ")
    for x in range (0,int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is now complete")
    print(myList)
                
            
        
                
def indexValues():
    try:
        Index = input("What index position do you wanna look for?     ")
        print(myList[int(Index)])
    except ValueError:
        print("Can you try again something again? Something must have happened")



def randomSearch():
    print("here is a  random value from your list.")
    print(myList[int(random.randint(0,len(myList)-1))])




def linearSearch():
    print("Lets go find a number in your list")
    num = input("What number would you like to find?     ")
    for x in range (len(myList)):
        if myList[x] == int(num):
            print("Your Number is at the position {} ".format(x))


def howMany():
    print("Lets find out how many of a specific number ar in your list")
    Num7 = input("What number would you like to find?     ")
    for x in range (len(myList)):
        if myList[x] == int(Num7):
            CountList.append(42)
    print("You have this many {}'s in your list".format(Num7))
    print(len(CountList))
    
    
if __name__ == "__main__":
    mainProgram()
