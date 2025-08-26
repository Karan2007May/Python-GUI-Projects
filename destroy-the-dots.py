#Imports
from guizero import Waffle, App, Text, PushButton
from random import randint

#variables
GRID_SIZE = 5
score = 0
red_dots = 0

#functions

def add_dot():
    global red_dots
    x,y = randint(0,GRID_SIZE-1), randint(0,GRID_SIZE-1)
    while board[x, y].dotty == True:
        x, y = randint(0, GRID_SIZE-1), randint(0, GRID_SIZE-1)
    board[x, y].dotty = True
    board.set_pixel(x,y, "red")
    red_dots += 1
    count.value = "No. of red dots = " + str(red_dots)

    speed = 1000
    if score > 30:
        speed = 200
    elif score > 20:
        speed = 400
    elif score > 10: 
        speed = 500
    
    if red_dots > 15:
        speed = 100
    elif red_dots > 10:
        speed = 300
    elif red_dots > 5:
        speed = 500

    all_red = True
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            if board[x, y].color != "red":
                all_red = False

    if all_red:
        message.value = "You lost! Score: " + str(score)
        board.disable()
        reset_button.show()
    else:
        board.after(speed, add_dot)

def destroy_dot(x,y):
    global score
    global red_dots
    if board[x, y].dotty == True:
        board[x, y].dotty = False
        board.set_pixel(x, y, "white")
        score += 1
        message.value = "Your score is " + str(score)
        red_dots -= 1
        count.value = "No. of red dots = " + str(red_dots)

def reset():
    global score
    global red_dots 
    score = 0
    red_dots = 0
    for x in range(GRID_SIZE):
        for y in range(GRID_SIZE):
            board[x, y].dotty = False
            board.set_pixel(x, y, "white")
    message.value = "Your score is " + str(score)
    count.value = "No. of red dots = " + str(red_dots)
    board.enable()
    reset_button.hide()
    board.after(1000, add_dot)

#App
app = App("Destroy the Dots",
          bg = "#FFFFFF")

instructions = Text(app,"Click the dots \nto destroy them",
                    size = 40,
                    color = "#40FF00",
                    font = "impact")

board = Waffle(app, height = GRID_SIZE, width = GRID_SIZE,
               command = destroy_dot)
board.after(1000, add_dot)

message = Text(app, "Your score is " + str(score),
               size = 30,
               color = "#00BBFF",
               font = "times new roman",
               underline = True)

count = Text(app, "No. of red dots = " + str(red_dots),
             size = 20,
             color = "#0044FF",
             font = "times new roman",
             italic = True)


reset_button = PushButton( app, command = reset, text = "Reset the Game", visible = False)
reset_button.bg = "green"
reset_button.text_color = "white"
reset_button.text_bold = True

app.display()