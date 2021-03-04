import random

theBoard = {'7': ' ' , '8': ' ' , '9': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '1': ' ' , '2': ' ' , '3': ' ' }
quotes = ["You are valued.",
       "You deserve the world.",
       "You day deserves to be amazing.",
       "You are enough.",
       "You dont need to change.",]
board_keys = []
for key in theBoard:
    board_keys.append(key)
def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
                        
    


print("Im a bored Bunny")
name = input ("What is your name?     ")
y = input ("thats a Beautiful Name, I like the name " +name+ " how are you today?    ")

if y == "sad":
        quote = input("Im sorry " + name + " do you want an uplifting quote?     ".format(name))
        if quote == "yes":
            while True:
                quote = input("Im sorry " + name + " do you want an uplifting quote?     ".format(name))
                if quote == "yes":
                    for x in range (0,1):
                        quote1 = quotes.pop(random.randint(0,len(quotes)))
                        print (quote1)
                    Better = input("are you feeling better?      ")
                    if Better == "no":
                        another = input("Im so sorry, would you like another quote?       ")
                        if another == "no":
                            print("Okay well i hope your day gets better.")
                            break
                        elif another == "yes":
                            print("Okay getting another quote for you now.")

                        else:
                            tryagin = input("im sorry i cant understand please reply with a 'yes' or 'no'        ")
                            if tryagain == "yes":
                                print("okay getting another quote for you now.")
                            else:
                                print("okay i hope to see you again.")
                                break
                    else:
                        print("Im so glad, come on back if you ever need another quote! ^-^")
                        break
        else:
            print("thats okay, I hope that you come try one again soon.")
elif y == "happy":
    print("That is so cool, I hope you have an amazing day!")
    game = input("Do you wanna play a game?")
    if game == "yes":
            print("To borad goes left to right, top to bottom for you piece placement")
            turn = 'X'
            count = 0


            for i in range(10):
                printBoard(theBoard)
                print("It's your turn," + turn + ". Move to which place?")

                move = input()        

                if theBoard[move] == ' ':
                    theBoard[move] = turn
                    count += 1
                else:
                    print("That place is already filled.\nMove to which place?")
                    continue

                # Now we will check if player X or O has won,for every move after 5 moves. 
                if count >= 5:
                    if theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': # across the top
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")                
                        break
                    elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': # across the middle
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
                    elif theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': # across the bottom
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
                    elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': # down the left side
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
                    elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ': # down the middle
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
                    elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': # down the right side
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break 
                    elif theBoard['7'] == theBoard['5'] == theBoard['3'] != ' ': # diagonal
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break
                    elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': # diagonal
                        printBoard(theBoard)
                        print("\nGame Over.\n")                
                        print(" **** " +turn + " won. ****")
                        break 

        # If neither X nor O wins and the board is full, we'll declare the result as 'tie'.
                if count == 9:
                    print("\nGame Over.\n")                
                    print("It's a Tie!!")

        # Now we have to change the player after every move.
                if turn =='X':
                    turn = 'O'
                else:
                    turn = 'X'        
    
            # Now we will ask if player wants to restart the game or not.
            restart = input("Do want to play Again?(y/n)")
            if restart == "y" or restart == "Y":  
                for key in board_keys:
                    theBoard[key] = " "

                game()
            

else:
    print ("I'm so sorry, I dont know what" +y+ "is, i hope you are doing okay though.")
