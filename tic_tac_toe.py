# we need a board 
# function : play game , check win , check tie , flip payer

board=["-","-","-",
       "-","-","-",
       "-","-","-",]
game=True
winner=None
c_player="X"

def display_board():
    print(board[0]+"|"+board[1]+"|"+board[2])
    print(board[3]+"|"+board[4]+"|"+board[5])
    print(board[6]+"|"+board[7]+"|"+board[8])

def play():
    # here we dispay initial board
    display_board()
    while game:
        turn(c_player)
        check_game_over()
        flip_player()
    if(winner=="X" or winner=="O"):
        print (winner +" won ")
    elif winner==None:
        print("tie ")

def turn(player):
    print(player + "'s turn ")
    p=input("Choose a position from 1 to 9 : ")
    valid= False
    while not valid :
        
        while p not in ["1", "2", "3", "4", "5", "6", "7", "8","9"] :
            p=input("invalid input ")
        p=int(p)-1
        if board[p] == "-" :
            valid=True
        else:
             print( "the spot is taken ")

        board[p]=player
        display_board()

def check_game_over():
    check_win()
    check_tie()

def check_win():
    global winner
    # check rows , colums and diagonals 
    row_winner=check_row()
    col_winner=check_coloane()
    di_winner=check_diagonala()

    if row_winner:
        winner=row_winner
    elif col_winner:
        winner=col_winner
    elif di_winner:
        winner=di_winner
    else:
        winner=None
    return

def check_row():
    global game
    row1=board[0]==board[1]==board[2] != "-"
    row2=board[3]==board[4]==board[5] != "-"
    row3=board[6]==board[7]==board[8] != "-"
    if row1 or row2 or row3 :
        game = False
    if row1:
        return board[0]
    elif row2:
        return board[3]
    elif row3:
        return board[6]
      
    return 

def check_coloane():
    global game
    col1=board[0]==board[3]==board[6] != "-"
    col2=board[1]==board[4]==board[7] != "-"
    col3=board[2]==board[5]==board[8] != "-"
    if col1 or col2 or col3 :
        game= False
    if col1:
        return board[0]
    elif col2:
        return board[1]
    elif col3:
        return board[2]
    
    return 

def check_diagonala():
    global game
    di1=board[0]==board[4]==board[8] != "-"
    di2=board[2]==board[4]==board[6] != "-"
    if di1 or di2 :
        game= False
    if di1:
        return board[0]
    elif di2 :
        return board[2]

    return

def check_tie():
    global game
    if "-" not in board:
        game=False
    return 

def flip_player():
    global c_player
    if c_player== "X" :
        c_player= "O"
    elif c_player== "O":
        c_player= "X"
    return 


play()


