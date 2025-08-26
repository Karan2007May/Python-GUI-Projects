#Imports
from guizero import App, Waffle, Text, PushButton, info
from random import choice

#Variables
colours = ["magenta", "purple", "red", "yellow", "green", "cyan"]
board_size = 14
moves_limit = 25
moves_taken = 0


#Functions
def flood(x, y, target, replacement):
    if target == replacement:
        return False
    if board.get_pixel(x,y) != target:
        return False
    board.set_pixel(x, y, replacement)
    if y+1 <= board_size-1:
        flood (x, y+1, target, replacement)
    if y-1 >= 0:
        flood (x, y-1, target, replacement)
    if x+1 <= board_size-1:
        flood (x+1, y, target, replacement)
    if x-1 >= 0:
        flood (x, y+1, target, replacement)

def all_squares_are_the_same():
    squares = board.get_all()
    if all(colour == squares[0] for colour in squares): 
        return True
    else:
        return False

def win_check():
    global moves_taken
    moves_taken += 1
    moves.value = "Moves Left: " + str(moves_limit - moves_taken)
    if moves_taken < moves_limit:
        if all_squares_are_the_same():
            win_text.value = "You Win!"
            palette.disable()
            reset_button.show()
    else:
        win_text.value = "You lost :("
        palette.disable()
        reset_button.show()

def fill_board():
    [board.set_pixel(x, y, choice(colours)) for y in range(board_size) for x in range(board_size)]

def init_palette():
    [palette.set_pixel(x, 0, colours[x]) for x in range(len(colours))]

def start_flood(x,y):
    flood_colour = palette.get_pixel(x,y)
    target = board.get_pixel(0,0)
    flood(0, 0, target, flood_colour)
    win_check()

def reset():
    global moves_taken
    moves_taken = 0
    moves.value = "Moves Left: " + str(moves_limit - moves_taken)
    win_text.value = ""
    palette.enable()
    reset_button.hide()
    fill_board()

def inform():
    app.info("How to play", "How to Play \n\n 1. To win this game, you need to paint the board with same colour \n\n 2. To paint the board select a colour from palette\n\n 3.Select the colour which is similar to adjacent colours of the colour of top right element and its sequence. \n\n 4. The colurs will flood with its adjacent colours.")

#App
app = App("Flood it", bg = "#fdfdd0")

title = Text(app, "Flood It", size = 30, bold = True, font = "impact")

board = Waffle(app, height = board_size, width = board_size, pad = 0)

palette = Waffle(app, width = len(colours), height = 1, dotty = True, command = start_flood)

moves = Text(app, "Moves Left: " + str(moves_limit - moves_taken))

win_text = Text(app)

info_button = PushButton(app, command = inform, text= "How to Play")
info_button.bg = "blue"
info_button.text_color = "white"
info_button.text_bold = True

reset_button = PushButton( app, command = reset,  text = "Reset the Game", visible = False)
reset_button.bg = "green"
reset_button.text_color = "white"
reset_button.text_bold = True


fill_board()
init_palette()

app.display()