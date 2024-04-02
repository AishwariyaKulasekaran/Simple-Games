# Tic-Tac-Toe
import sys,random,time
print(" welcome to Tic-Tac-Toe Game ")
game_active = True
computer_player= 'X'
current_player = 'X'

# Creating board for game
fields = [" ",
             "1","2","3",
             "4","5","6",
             "7","8","9"]

# This function prints the board
def display_board():
    print (fields[1] + "|" + fields[2] + "|" + fields[3]  )
    print (fields[4] + "|" + fields[5] + "|" + fields[6] )
    print (fields[7] + "|" + fields[8] + "|" + fields[9] )
  
# Getting user input and verifying the game flow based on input
def player_input(choice):
    global game_active    
    while True:        
        
        if choice==1:
            if current_player=="computer":
                time.sleep(1)
                field_no=random.randint(1,9)
            else:
                #field_no = player_input()
                field_no = input("Enter the field no pls: ") 
        elif choice==2:
            #field_no = player_input()
             field_no = input("Enter the field no pls: ")
            
        #field_no = input("Enter the field no pls: ")    
        try:
          field_no = int(field_no)
        #Checks if the input entered is valid type
        except ValueError:
            if type(field_no)==str:
                print("Oops! Game Terminated")
      
        # Ending the game early by the player by entering quit
        if field_no == 'q':
            game_active = False          
            return    
                   
        else:
            """if field_no >= 1 and field_no <= 9:
                if fields[field_no] == 'X' or fields[field_no] == 'O':
                    print("The field number entered is already occupied.\nPls enter another number")
                else:
                    return field_no
            else:
                print("Enter a number between 1 to 9")"""
                
            if current_player=="computer":
                if field_no >= 1 and field_no <= 9:
                    if fields[field_no] == 'X' or fields[field_no] == 'O':
                        field_no=random.randint(1,9)
                    else:
                        return field_no
                else:
                    print("Enter a number between 1 to 9")
            else:
                if field_no >= 1 and field_no <= 9:
                    if fields[field_no] == 'X' or fields[field_no] == 'O':
                        print("The field number entered is already occupied.\nPls enter another number")
                    else:
                        return field_no
                else:
                    print("Enter a number between 1 to 9")
                


#Switching between players 
"""def switch_player():
    global current_player
    if current_player == 'X':
        current_player = 'O'
    else:
        current_player = 'X'"""
def switch_player():
    global current_player
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
      
# Checking for winning conditions
def check_won():
    # when all 3 fields are same the respective player has won the game
  
    # check for rows
    if fields[1] == fields[2] == fields[3]:
        return fields[1]
    elif fields[4] == fields[5] == fields[6]:
        return fields[4]
    elif fields[7] == fields[8] == fields[9]:
        return spielfeld[7]
    # check for columns
    elif fields[1] == fields[4] == fields[7]:
        return fields[1]
    elif fields[2] == fields[5] == fields[8]:
        return fields[2]
    elif fields[3] == fields[6] == fields[9]:
        return fields[3]
    # check for diagonals
    elif fields[1] == fields[5] == fields[9]:
        return fields[5]
    elif fields[7] == fields[5] == fields[3]:
        return fields[5]

def check_draw():
    if (fields[1] == 'X' or fields[1] == 'O') \
      and (fields[2] == 'X' or fields[2] == 'O') \
      and (fields[3] == 'X' or fields[3] == 'O') \
      and (fields[4] == 'X' or fields[4] == 'O') \
      and (fields[5] == 'X' or fields[5] == 'O') \
      and (fields[6] == 'X' or fields[6] == 'O') \
      and (fields[7] == 'X' or fields[7] == 'O') \
      and (fields[8] == 'X' or fields[8] == 'O') \
      and (fields[9] == 'X' or fields[9] == 'O'):
        return ('draw')
# Main game loop starts here
# Print the current game board
display_board()
print("\nInstruction: \nIf you wish to continue game enter a number else terminate the game by entering q \n")
player_choice=int(input("Choose your opponent \n1.Computer \n2.Another Player \nEnter your choice: "))
if player_choice==2:
    player1=input("\nEnter player1 name:")
    player2=input("\nEnter player2 name:")
    current_player=player1
else:
    print("\nYou chose computer as your opponent")
    player1="computer"
    player2=input("\nEnter your name:")
    current_player=player1
    
while game_active:
    # Input of the active player
    #print()
    print ("Player " + current_player + " turn")
    """if player_choice==1:
        if current_player=="computer":
            field_no=random.randint(1,9)
        else:
            field_no = player_input()
    elif player_choice==2:
        field_no = player_input()"""

    field_no = player_input(player_choice)
    
    if field_no:
        #marks the field no with X or O
        if current_player==player1:
            #changes the values in the fields list ie board
            #fields[field_no] = 'X'
            fields[field_no] = "X"
        else:
            fields[field_no] = "O"
      
        # print current game board
        display_board()
      
        # Check if any player has won
        won = check_won()
        
        if won=="X":
            print ("Player " + player1 + " has won the game!")
            game_active = False
            break
        elif won=="O":
            print ("Player " + player2 + " has won the game!")
            game_active = False
            break
          
        # Check for a draw
        draw = check_draw()
        if draw:
            print ("Game is draw")
            game_active = False
          
        # To switch between the player
        switch_player()
    else:
        print("Goodbye")
        sys.exit()
#print() 
