"""
Program Goals:
Do the things
"""
import random

myList = []
CountList = []
uniqueList = []

print("Hello, there! Lets work with some lists today")
#IM USUING THIS FOR MY COMMENTS AS IT HELPS WITH COLORING! I AM SORRY IF THIS
#DOCS MY GRADE BUT IM NOT BUDGING. ALSO TO AGAIN HELP WITH MY PROCESSING.
#THESE LINES WILL ONLY BE SO LONG AS TO NOT HAVE A SCROLLER AT THE BOTTOM
#NOW LETS BEGIN


#This is just the menu, It just lets you move around the rest of the program.

def mainProgram():
    while True:
        print("Choose one of the following options. Type a number ONLY")
        choice = input("""1. Add Numbers to your list (2 methods)

2. Find a Number in Your original list (4 methods)

3. Use Binary Searches, this will sort your list.(2 Methods)

4. Basic list functions (3 Methods)

5. Bet the computer that You can find the mystery number

6. Quit the progam.    """)



        if choice == "1":
            Adding = input("""How do you want to Add things to your list?
1. Add Specific Numbers
2. Add a Bunch of numbers       """)
            if Adding == "1":
                addToList()
            elif Adding == "2":
                addABunch()




        elif choice == "2":
            Search = input("""How do you want to find a number?
1. Find the number At a certian index position
2. Look through your entire list and find all of one number
3. Find out how many of one number are in your list
4. Find a random number in your list""")
            if Search == '1':
                indexValues()
            elif Search =='4':
                randomSearch()
            elif Search == '3':
                howMany()
            else:
                linearSearch()




        elif choice == '3':
            sortList()
            Binary = input("""How do you want to find your Number?
1. Using recursion that runs a loop untill it finds your number
2. Using iterative searching that does the same thing however has no chance of crashing""")
            if Binary == '1':
                binSearch = input("What number are you looking for?    ")
                recursiveBinarySearch(uniqueList, 0, len(uniqueList)-1, int(binSearch))
            elif Binary == '2':
                coreSearch = input("What number are you looking for?    ")
                result = IBS(uniqueList, int(coreSearch))
                if result !=-1:
                    print("Your number is at index position {}".format(result))
                else:
                    print("your number isnt it this list sorry.")
                
        
        elif choice == "4":
            Basic = input("""What list function do you want to use?
1. Print your list
2. Add your list together and find the total value
3. Clear your list""")
            if Basic == "1":
                printLists()
            elif Basic == "2":
                AddTogether()
            else:
                myList.clear()
                uniqueList.clear()
                print("You are all set")
        elif choice == '5':
            Bet()
        elif choice =="6":
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


#This is Just a way for you to add numbers with a error catcher, It asks you
#What you want to add then it does it, If you have a number and it is above 0
#If those conditions are not met, it gives you an error Message and asks you
#If you want to rety
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

#This function uses a random number generator to make the process of adding
#Lots of numbers easier. 
def addABunch():
    print("Here we can add a bunch of numbers to the list")
    numToAdd = input("How many numbers do you want to add?    ")
    numRange = input("How high do you want the numbers to go?   ")
    for x in range (0,int(numToAdd)):
        myList.append(random.randint(0,int(numRange)))
    print("Your list is now complete")
    print(myList)
                
            
        
#This turly just uses one of lists primary functions which is index vaules. And
#A sprinkle of error catching
def indexValues():
    try:
        Index = input("What index position do you wanna look for?     ")
        print(myList[int(Index)])
    except ValueError:
        print("Can you try again something again? Something must have happened")


#This uses the same random number generator from above but this time to find
#You a random number
def randomSearch():
    print("here is a  random value from your list.")
    print(myList[int(random.randint(0,len(myList)-1))])



#This goes through your list number by number and finds all instances of a
#specified number
def linearSearch():
    print("Lets go find a number in your list")
    num = input("What number would you like to find?     ")
    for x in range (len(myList)):
        if myList[x] == int(num):
            print("Your Number is at the position {} ".format(x))
#Recursive binary search usuing the process of recursion to split your sorted
#List into multiple smaller lists that it tries to find a specified number
def recursiveBinarySearch(uniqueList, low, high, x):
    if high >= low:
        mid = (high + low) // 2
        if uniqueList[mid] == x:
            print("Oh what luck, your number is at position {}".format(mid))
        elif uniqueList[mid] > x :
            return recursiveBinarySearch(uniqueList, low, mid - 1, x)
        else:
            return recursiveBinarySearch(uniqueList, mid + 1, high, x)       
    else:
        print("Your number isnt here!")

#Iterave binary search does the same thing, however it doesn't use recursion
#Limiting the amount of bytes it takes to avoid your computer crashing.
def IBS(uniqueList, x):
    low = 0
    high = len(uniqueList)-1
    mid = 0

    while low <= high:
        mid = (high + low) // 2

        if uniqueList[mid] < x:
            low = mid + 1
        elif uniqueList[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

#This is the same as linear search however it doesnt show you the exact place
#Of each instance instead opting for just the final number
def howMany():
    print("Lets find out how many of a specific number ar in your list")
    Num7 = input("What number would you like to find?     ")
    for x in range (len(myList)):
        if myList[x] == int(Num7):
            CountList.append(42)
    print("You have this many {}'s in your list".format(Num7))
    print(len(CountList))
    CountList.clear()
#This program sorts your list into another list that has no duplicate numbers
#By simply ching if it is in the new list already. This is used to work with the
#Binary search methods
def sortList():
    for x in myList:
        if x not in uniqueList:
            uniqueList.append(x)
    uniqueList.sort()
    showme = input("Do you wanna see your new list? Y/N    ")
    if showme.lower() == 'y':
        print(uniqueList)
#This adds your list together to get you the total value of your list
def AddTogether():
    total = 0
    for x in range (0,len(myList)):
        total = total + myList[x]
    print("Your total value is {}".format(total))
    
#This uses just a simple print statement, with an if/elif statement to ask
#What list you want to display at the moment
def printLists():
    if len(uniqueList) == 0:
        print(myList)
    else:
        Which = input("What list sorted or unsorted  S/UNS     ")
        if Which.lower() == 's':
            print(uniqueList)
        else:
            print(myList)
#This just splits it up into two diffrent bet methods cause at first I was only
#Going to add one into the Program
def Bet():
    Who = input("Who should guess the Number?   You (Y) or the Computer (C)      ")
    if Who == 'Y':
        BetY()
    else:
        BetC()
#I FEEL SO PROUD^-^
#Okay so this uses the same process at the binary searches except it doesn't
#Know the number it is looking for. It splits the lists the same way,
#But its based off of user input at every step instead of just at the begging
def BetC():
    print("Okay think of a number Im gonna try and guess it. IT MUST BE A NUMBER ON YOUR LIST")
    sortList()
    low = 0
    high = len(uniqueList)-1
    for x in range(0,5):
        guess = (uniqueList[int(random.randint(low,high))])
        print(guess)
        correct = input("Is this your Number? (Y/N)    ")
        if correct == 'Y':
            Print("I win yay!")
        else:
            print("Maybe next time")
            HL = input("Is the number higher or lower then my guess?(H/L)    ")
            if HL == "H":
                low = guess + 1
            elif HL == "L":
                high = guess - 1
            
    print("I guess I couldnt find it")


#This is the same thing, But you are guessing, It isnt a neccesary step to sort
#The list because of how the brain procceses things. It simple creates a random
#Number and then tells your if your guess is higher or lower.
def BetY():
    print("""Hello, I bet you cant guess the number Im thinking ^-^
The two rules.
You get five chances then its game over,
It will of course be a number in your list""")
    magic = (myList[int(random.randint(0,len(myList)-1))])
    for x in range(0, 5):
        Guess = input("What is your guess?       ")
        if int(Guess) == magic:
            print("You found it!")
            mainProgram()
        elif int(Guess)> magic:
            print("""Try again your number is Lower

""")
        else:
            print("""Try higher this time

""")


    print("Oh no You lost your number waws acctually {}".format(magic))
    
#This magic thing is what tells the program to run
if __name__ == "__main__":
    mainProgram()
