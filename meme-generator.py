#Imports
from guizero import App, TextBox, Drawing, Combo, Slider

#Functions
def draw_meme():
    meme.clear()
    meme.image(0,0, "C:\\Users\\jivik\\OneDrive\\Desktop\\Rotaract Files\\Explore the colors of Rotaract (1)_prev_ui.png")
    meme.text(
        20,20, top_text.value, 
        color = color.value, 
        size = size.value,
        font = font.value)
    meme.text(
        20,320, bottom_text.value,
        color = color.value,
        size = size.value,
        font = font.value)

#App
app = App("Meme Generator")

#Other Widgets
top_text = TextBox (app, "top text", command=draw_meme)

bottom_text = TextBox(app, "bottom text", command = draw_meme)

color = Combo(app, 
              options = ["white", "black", "orange", "blue", "green", "red", "yellow"],
              selected = "blue",
              command = draw_meme)

font = Combo(app,
             options = ["verdana", "times new roman", "courier", "impact"],
             selected = "impact", 
             command = draw_meme)

size = Slider(app, start = 20, end = 40, command = draw_meme)

meme = Drawing(app, width = "fill", height = "fill")
draw_meme()


#App display
app.display()