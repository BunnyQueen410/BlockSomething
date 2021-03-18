"""
Program Goals:
Do the things
"""

#create functions that will perform those actions above
myList = []
import random

print("Hello, there! Lets work with some lists today")

def mainProgram():
    while True:
        print("Choose one of the following options. Type a number ONLY")
        choice = input("""1. Add to List,
2. Return the value at an index prosition.
3. Get a random value that you have inputted.
4. Quit the progam.    """)
        if choice == "1":
            addToList()
        elif choice == "2":
            indexValues()
        elif choice == "3":
            randomSearch()
        elif choice =="4":
            print(""" Okay Bye ^-^
  (\_/)
  (^_^)
 (____)0""")
            break
        else:
            print("Im sorry that wast an option, try again please. Remeber that you can only use 1,2,3,4")
            mainProgram()

def addToList():
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
                
            
        
                
def indexValues():
    try:
        Index = input("What index position do you wanna look for?     ")
        print(myList[int(Index)])
    except ValueError:
        print("Can you try again something again? Something must have happened")

def randomSearch():
    print("here is a  random value from your list.")
    print(myList[int(random.randint(0,len(myList)))])
    
    
    


if __name__ == "__main__":
    mainProgram()
