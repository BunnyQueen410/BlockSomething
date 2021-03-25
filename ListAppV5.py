"""
Program Goals:
Do the things
"""
import random

myList = []
CountList = []
uniqueList = []

print("Hello, there! Lets work with some lists today")

def mainProgram():
    while True:
        print("Choose one of the following options. Type a number ONLY")
        choice = input("""1. Add to List,
2. Add a bunch of Numbers
3. Return the value at an index prosition.
4. Get a random value that you have inputted.
5. Find where a number is in your list
6. Find out how many of one number is on your list
7. Clear your list and start again
8. Print your list
9. Organize your list
10. Add your list together
11. Quit the progam.    """)
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
            uniqueList.clear()
            print("You are all set")
        elif choice  == "8":
            printLists()
        elif choice == "9":
            sortList()
        elif choice == "10":
            AddTogether()
        elif choice =="11":
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
    CountList.clear()

def sortList():
    for x in myList:
        if x not in uniqueList:
            uniqueList.append(x)
    uniqueList.sort()
    showme = input("Do you wanna see your new list? Y/N    ")
    if showme.lower() == 'y':
        print(uniqueList)

def AddTogether():
    total = 0
    for x in range (0,len(myList)):
        total = total + myList[x]
    print("Your total value is {}".format(total))
    
    
def printLists():
    if len(uniqueList) == 0:
        print(myList)
    else:
        Which = input("What list sorted or unsorted  S/UNS     ")
        if Which.lower() == 's':
            print(uniqueList)
        else:
            print(myList)
if __name__ == "__main__":
    mainProgram()
