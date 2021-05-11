import tkinter
# хранилище изображений

#-----------------------------------переменные для хранения изображений-------------------------------------------------

title = []
playButton = []
mainMenu = []

#------------------------------------------инициализация переменных-----------------------------------------------------

def init():
    title.append(tkinter.PhotoImage(file="Images/title.png"))
    playButton.append(tkinter.PhotoImage(file="Images/playButton.png"))
    mainMenu.append(tkinter.PhotoImage(file="Images/Background.png"))