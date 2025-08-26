from guizero import App, Text, Picture

app = App("Wanted!")
app.bg = "#fbfbd0"

wanted_text = Text(app, "WANTED")
wanted_text.text_size = 50
wanted_text.text_color = "red"
wanted_text.font = "Impact"

wanted_image = Picture(app, image="C:\\Users\\jivik\\OneDrive\\Desktop\\Rotaract Files\\Explore the colors of Rotaract (1)_prev_ui.png")

app.display()