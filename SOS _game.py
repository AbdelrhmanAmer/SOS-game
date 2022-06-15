# game 0 --->  SOS GAME 
# the last number game (basic game)
# name: Abdelrhman Amer Ali  عبدالرحمن عامر علي
# Id: 20211060


# create board
board = ["-", "-", "-", "-",
         "-", "-", "-", "-", 
         "-", "-", "-", "-",
         "-", "-", "-", "-" ]
# my variables
# game is going to make the while loop go on until the game over
game_is_going = True

# to take s or o from players as string
input1 = "_"
input2 = "_"

# to take the position from user as intger
inp1 = -1
inp2 = -1

# to store the points when someone score
player1_points = 0
player2_points = 0

# to can switch turns 
turn = 0

# it will count 1 when any player will put any value in the board 
# by this variable i will check if the board is filled or not if count == 16 then the board is filleds
count = 0

S = "S"
O = "O"

# i will use too to swich the check turn 
current_player = 1

# display the board
def display_board():
    global player1_points, player2_points
    print("\n")   # i wanted to display it nicely :) 
    print(board[0] + " | " + board[1] + " | " + board[2] + " | " + board[3] + "        1 | 2 | 3 | 4")
    print(board[4] + " | " + board[5] + " | " + board[6] + " | " + board[7] + "        5 | 6 | 7 | 8")
    print(board[8] + " | " + board[9] + " | " + board[10] + " | " + board[11] + "        9 |10 |11 | 12" )
    print(board[12] + " | " + board[13] + " | " + board[14] + " | " + board[15] + "       13 |14 |15 | 16")
    print("\n")
    print (f"player 1'points = {player1_points}") # show the points of each player every time 
    print (f"player 2'points = {player2_points}")


 
#play the game
def play_the_game():
    global player1_points, player2_points
    # go a head while the board is not filled
    while game_is_going:
        # do this functions 
        display_board()
        take_input()
        check_wining()
        flip_the_player()
        check_if_game_over()
    
    # if the board is filled
    print("\n")# show result of the point 
    print (f"player 1'points = {player1_points}") 
    print (f"player 2'points = {player2_points}")
    print("\n")
    # and then print who won the game or there is a tie
    if player1_points > player2_points:
        print("player 1 wons")
    elif player2_points > player1_points:
        print("player 2 wons")
    else :
        print ("tie ")


# take input 
def take_input():
    global turn, inp1, inp2, current_player ,S ,O , input1, input2, count

    # first take input from player 1 
    # and i did if turn % 2 == 0 take the input, 
    # because if the player scored a point i will increse the turn by one and in line   i actually increase turn variable by 1 
    # so it has increased by two and 2 % 2 == 0 and player will go play again
    if turn % 2 == 0:
        input1 = input("player (1) Enter  S  or  O  : ").upper() # check of the input to avoid the error

        # if the input is valid ,
        if input1 == S or  input1 == O:
            # then take the position 
            inp1 = int(input("player number (1) please Enter position: "))
            inp1 = inp1 - 1 # subtract the postion by one to put it in the board 

            # check if the position is filled or out of range 
            if inp1 not in range(0, 16) or board[inp1] != "-" :
                print ("please enter a valid input")
                # come back and enter a right postion the next time 
                return take_input()
            else:
                # else if it is a correct position then put it in the board 
                board[inp1] = input1 

                # add one to turn to flip the player next role 
                turn += 1  
                count += 1
        else:# if the value is not correct then try again
            print("valid input :( please try again ") 
            return take_input()

    elif turn % 2 == 1:# it is the same as before but this for player 2
        input2 = input("player (2) Enter  S  or  O  : ").upper()
        if input2 == S or  input2 == O:
            inp2 = int(input("player number (2) please Enter position: "))
            inp2 = inp2 - 1
            if inp2 not in range(0, 16) or board[inp2] != "-" :
                print ("please enter a valid input")
                return take_input()
            else:
                board[inp2 ] = input2  
                turn += 1 
                count += 1
        else:
            print("valid input :( please try again ") 
            return take_input()            
        
# check of win
def check_wining():
    check_horizontal()
    check_verticall()
    check_digonal()


# check horizontal
# the check in this game is quite complexed 
# if i want to Enter a position and want to ckeck form it 
# i have to specify the if conditions 
# that's what i am gonna to explain to you in next coming lines
def check_horizontal():
    global inp1 , inp2 , player1_points , player2_points, current_player, S, O, input1, input2, turn
    # first it's player1's turn 
    if current_player == 1:
        if input1 == S:# if player1' input is (S)

            # board = ["0", "1", "_", "_",
            #          "4", "5", "_", "_", 
            #          "8", "9","_","_",
            #         "12","13","_","_" ]  here i will check if the input is in any place of this places 
            if inp1 == 0 or inp1 == 1 or inp1 == 4 or inp1 == 5 or inp1 == 8 or inp1 == 9 or inp1 == 12 or inp1 == 13 :
                # then check if there is a score, if the value of position + 2 == S , and the value of positoin + 1 == O
                if board[inp1] == board[inp1 + 2] == S and board[inp1 + 1] == O:
                    player1_points += 1 # then make points increase by one 
                    turn += 1 # then make turn increases by one and that to make the player again (i explained it in line 80 ) 

            # board = ["_", "_", "2", "3",
            #          "_", "_", "6", "7", 
            #          "_", "_","10","11",
            #          "_", "_","14","15" ] # if input input in one of those places 
            elif inp1 == 3 or inp1 == 2 or inp1 == 7 or inp1 == 6 or inp1 == 11 or inp1 == 10 or inp1 == 15 or inp1 == 14 :
                # then check if there is a score, if the value of position - 2 == S , and the value of positoin - 1 == O
                if board[inp1] == board[inp1 - 2] == S and board[inp1 - 1] == O:
                    player1_points += 1
                    turn += 1

        elif input1 == O:
            # # if player1's input == (O)

            # board = ["_", "1", "2", "_",
            #          "_", "5", "6", "_", 
            #          "_", "9","10", "_",
            #          "_", "13","14","_" ] if input is in one of those places 
            if inp1 == 1 or inp1 == 2 or inp1 == 5 or inp1 == 6 or inp1 == 9 or inp1 == 10 or inp1 == 13 or inp1 == 14 :
                # then check of the position before and after input is S
                if board[inp1 + 1] == board[inp1 - 1] == S:
                    player1_points += 1
                    turn += 1


    elif current_player == 2: # that is the same check but this for player 2
        if input2 == S:
            if inp2 == 0 or inp2 == 1 or inp2 == 4 or inp2 == 5 or inp2 == 8 or inp2 == 9 or inp2 == 12 or inp2 == 13 :
                if board[inp2] == board[inp2 + 2] == S and board[inp2 + 1] == O:
                    player2_points += 1
                    turn += 1
            elif inp2 == 3 or inp2 == 2 or inp2 == 7 or inp2 == 6 or inp2 == 11 or inp2 == 10 or inp2 == 15 or inp2 == 14 :
                if board[inp2] == board[inp2 - 2] == S and board[inp2 - 1] == O:
                    player2_points += 1
                    turn += 1
        elif input2 == O:         
            if inp2 == 1 or inp2 == 2 or inp2 == 5 or inp2 == 6 or inp2 == 9 or inp2 == 10 or inp2 == 13 or inp2 == 14 :
                if board[inp2 + 1] == board[inp2 - 1] == S:
                    player2_points += 1
                    turn += 1

# check verticall
def check_verticall():
    global inp1 , inp2 , player1_points , player2_points, current_player, S, O, input1, input2, turn
    if current_player == 1:
        if input1 == S:# if player1' input is (S)

            # board = ["0", "1", "2", "3",
            #          "4", "5", "6", "7", 
            #          "_", "_", "_", "_",
            #          "_", "_", "_", "_" ] if the input is one of those places
            if inp1 == 0 or inp1 == 4 or inp1 == 1 or inp1 == 5 or inp1 == 2 or inp1 == 6 or inp1 == 3 or inp1 == 7 :
                # check if the value of the position after the input in column == O and the value after the O == S
                if board[inp1] == board[inp1 + 8] == S and board[inp1 + 4] == O:
                    player1_points += 1
                    turn += 1

            # board = ["_", "_", "_", "_",
            #          "_", "_", "_", "_", 
            #          "8", "9", "10","11",
            #          "12","13","14","15"]  if the input is one of those places
            elif inp1 == 12 or inp1 == 8 or inp1 == 13 or inp1 == 9 or inp1 == 14 or inp1 == 10 or inp1 == 15 or inp1 == 11 :
                # check if the value of the position before the input in column == O and the value before the O == S
                if board[inp1] == board[inp1 - 8] == S and board[inp1 - 4] == O:
                    player1_points += 1
                    turn += 1

        elif input2 == O:# if player1's input == (O)

            # board = ["_", "_", "_", "_",
            #          "4", "5", "6", "7", 
            #          "8", "9","10","11",
            #          "_", "_","_","_" ]  if the input is one of those places
            if inp1 == 4 or inp1 == 8 or inp1 == 5 or inp1 == 9 or inp1 == 6 or inp1 == 10 or inp1 == 7 or inp1 == 11 :
                if board[inp1 - 4] == board[inp1 + 4] == S:
                    player1_points += 1
                    turn += 1


    elif  current_player == 2: # that is the same check but this for player 2
        if input2 == S:
            if inp2 == 0 or inp2 == 4 or inp2 == 1 or inp2 == 5 or inp2 == 2 or inp2 == 6 or inp2 == 3 or inp2 == 7 :
                if board[inp1] == board[inp1 + 8] == S and board[inp1 + 4] == O:
                    player2_points += 1
                    turn += 1
            elif inp2 == 12 or inp2 == 8 or inp2 == 13 or inp2 == 9 or inp2 == 14 or inp2 == 10 or inp2 == 15 or inp2 == 11 :
                if board[inp2] == board[inp2 - 8] == S and board[inp2 - 4] == O:
                    player2_points += 1
                    turn += 1

        elif input2 == O:
            if inp2 == 4 or inp2 == 8 or inp2 == 5 or inp2 == 9 or inp2 == 6 or inp2 == 10 or inp2 == 7 or inp2 == 11 :
                if board[inp2 - 4] == board[inp2 + 4] == S:
                    player2_points += 1
                    turn += 1

# check digonal
def check_digonal():
    global inp1 , inp2 , player2_points , player1_points, current_player, S, O, input1, input2, turn
    if current_player == 1:
        if input1 == S: # if player1's input == (S)

            # board = ["0", "1", "_", "_",
            #          "4", "5", "_", "_", 
            #          "_", "_", "_", "_",
            #          "_", "_", "_", "_" ]  if the input is one of those places
            if inp1 == 0 or inp1 == 1 or inp1 == 4 or inp1 == 5 :
                # check from the next value in the digonal if it == O , and if the next of O == S
                if board[inp1] == board[inp1 + 10] == S and board[inp1 + 5] == O:
                    player1_points += 1
                    turn += 1

            # board = ["_", "_", "_", "_",
            #          "_", "_", "_", "_", 
            #          "_", "_", "10", "11",
            #          "_", "_", "14", "15" ]         
            elif inp1 == 10 or inp1 == 15 or inp1 == 14 or inp1 == 11 :
                # check from the value before the input in digonal if it == O , and if the before the O == S
                if board[inp1] == board[inp1 - 10] == S and board[inp1 - 5] == O:
                    player1_points +=1
                    turn += 1

            # board = ["_", "_", "2", "3",
            #          "_", "_", "6", "7", 
            #          "_", "_", "_", "_",
            #          "_", "_", "_", "_" ]  if the input is one of those places        
            elif inp1 == 2 or inp1 == 3 or inp1 == 6 or inp1 == 7 :
                # same logic as before
                if board[inp1] == board[inp1 + 6] == S and board[inp1 + 3] == O:
                    player1_points += 1
                    turn += 1
            
            # board = ["_", "_", "_", "_",
            #          "_", "_", "_", "_", 
            #          "8", "9", "_", "_",
            #          "12","13", "_", "_" ] if the input is one of those places 
            elif inp1 == 8 or inp1 == 12 or inp1 == 9 or inp1 == 13 :
                # same logic as before
                if board[inp1] == board[inp1 - 6] == S and board[inp1 - 3] == O:
                    player1_points += 1
                    turn += 1

        elif input1 == O:
            if inp1 == 5 or inp1 == 6 or inp1 == 9 or inp1 == 10:
                if board[inp1 - 5] == board[inp1 + 5] == S:
                    player1_points += 1
                    turn += 1
                elif board[inp1 - 3] == board[inp1 + 3] == S:
                    player1_points += 1
                    turn += 1

    elif current_player == 2:
        if input2 == S:
            if inp2 == 0 or inp2 == 1 or inp2 == 4 or inp2 == 5 :
                if board[inp2] == board[inp2 + 10] == S and board[inp2 + 5] == O:
                    player2_points += 1
                    turn += 1
            elif inp2 == 10 or inp2 == 15 or inp2 == 14 or inp2 == 11 :
                if board[inp2] == board[inp2 - 10] == S and board[inp2 - 5] == O:
                    player2_points +=1
                    turn += 1
            elif inp2 == 2 or inp2 == 3 or inp2 == 6 or inp2 == 7 :
                if board[inp2] == board[inp2 + 6] == S and board[inp2 + 3] == O:
                    player2_points += 1
                    turn += 1
            elif inp2 == 8 or inp2 == 12 or inp2 == 9 or inp2 == 13 :
                if board[inp2] == board[inp2 - 6] == S and board[inp2 - 3] == O:
                    player2_points += 1
                    turn += 1
        elif input2 == O:
            if inp2 == 5 or inp2 == 6 or inp2 == 9 or inp2 == 10:
                if board[inp2 - 5] == board[inp2 + 5] == S:
                    player2_points += 1
                    turn += 1
                elif board[inp2 - 3] == board[inp2 + 3] == S:
                    player2_points += 1
                    turn += 1

# check if game over
def check_if_game_over():
    global game_is_going , count
    if count == 16:
        game_is_going = False

# fliping the player 
def flip_the_player():
    global current_player, turn
    if turn % 2 == 1:
        current_player = 2
    else:
        current_player = 1
play_the_game()