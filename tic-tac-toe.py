#Imports -------------------------
from guizero import App, Box, PushButton, Text

#Functions ------------------------

def clear_board():
    new_board = [[None, None, None], 
                 [None, None, None], 
                 [None, None, None]]
    for x in range(3):
        for y in range(3):
            button = PushButton(
                board, text = "", grid = [x, y], width = 3,
                command = choose_square, args = [x,y]
            )
            button.text_bold = True
            button.text_color = "#000000"
            button.bg = "white"
            button.text_size = 20
            new_board[x][y] = button
    return new_board

def choose_square(x,y):
    board_squares[x][y].text = turn
    board_squares[x][y].disable()
    toggle_player()
    check_win()

def toggle_player():
    global turn
    if turn == "X":
        turn = "O"
    else:
        turn = "X"
    message.value = "It is your turn, " + turn

def check_win():
    winner = None

    #Vertical lines
    if(
        board_squares[0][0].text == board_squares[0][1].text == board_squares[0][2].text
    ) and board_squares[0][2].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif(
        board_squares[1][0].text == board_squares[1][1].text == board_squares[1][2].text
    ) and board_squares[1][2].text in ["X", "O"]:
        winner = board_squares[1][0]
    elif(
        board_squares[2][0].text == board_squares[2][1].text == board_squares[2][2].text
    ) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[2][0]

    #Horizontal lines
    elif(
        board_squares[0][0].text == board_squares[1][0].text == board_squares[2][0].text
    ) and board_squares[2][0].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif(
        board_squares[0][1].text == board_squares[1][1].text == board_squares[2][1].text
    ) and board_squares[2][1].text in ["X", "O"]:
        winner = board_squares[0][1]
    elif(
        board_squares[0][2].text == board_squares[1][2].text == board_squares[2][2].text
    ) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[0][2]

    #Diagonals
    elif(
        board_squares[0][0].text == board_squares[1][1].text == board_squares[2][2].text
    ) and board_squares[2][2].text in ["X", "O"]:
        winner = board_squares[0][0]
    elif(
        board_squares[0][2].text == board_squares[1][1].text == board_squares[2][0].text
    ) and board_squares[2][0].text in ["X", "O"]:
        winner = board_squares[0][2]
    
    if winner is not None:
        message.value = winner.text + " wins!"
        reset_button.show()

    elif moves_taken() == 9:
        message.value = "It's a draw"
        reset_button.show()

def moves_taken():
    moves = 0
    for row in board_squares:
        for col in row:
            if col.text == "X" or col.text == "O":
                moves += 1
    return moves

def reset():
    global board_squares
    board_squares = clear_board()
    reset_button.hide()
    message.value = "It is your turn, " + turn

#Variables----------------------------
turn = "X"
board_squares = []

#App-------------------------------------
app = App("Tic Tac Toe", bg = "#fbfbd0")

title = Text( app, text = "Tic-Tac-Toe",
              color = "red", 
              font = "impact", 
              size = 50,
              bold = True, 
              underline = True)
board = Box(app, layout = "grid")
board.border = 10
board_squares = clear_board()
message = Text(app, text = "It is your turn, " + turn,
               italic = True,
               font = "times new roman",
               size = 30,
               color = "black")
reset_button = PushButton( app, command = reset, text = "Reset the Game", visible = False)
reset_button.bg = "green"
reset_button.text_color = "white"
reset_button.text_bold = True


app.display()