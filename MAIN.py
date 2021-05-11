import tkinter
import ImageManager
import MainMenu


def draw_title(_canvas):
    _canvas.create_image(0, 0, anchor="nw", image=ImageManager.title[0])
    r = _canvas.create_image(175, 420, anchor="nw", image=ImageManager.playButton[0])
    _canvas.tag_bind(r, '<Button-1>', lambda event: print('works'))


def open_menu():
    pass


window = tkinter.Tk()
ImageManager.init()
currentGame = MainMenu.Instance

canvas = tkinter.Canvas(window, width=800, height=600)
canvas.pack()
draw_title(canvas)



window.mainloop()