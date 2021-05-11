import tkinter
import ImageManager
from MainMenu import Instance as mainMenu
from MainMenu import currentGame
# собсна главный скрипт: инициализация окна и вызов команд обновления классов

#----------------------------------------------функции------------------------------------------------------------------

def close_window():
    #функция для отслеживания закрытия приложухи
    running = False

#-----------------------------------------инициализация окна------------------------------------------------------------


window = tkinter.Tk()
ImageManager.init()
window.protocol("WM_DELETE_WINDOW", close_window)
running = True
canvas = tkinter.Canvas(window, width=800, height=600)
canvas.pack()
mainMenu.Start(canvas)

#----------------------------------------покадровая обработка-----------------------------------------------------------

window.mainloop()
while running:
    currentGame.Update(canvas)