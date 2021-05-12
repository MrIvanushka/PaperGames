from tkinter import *
import random

root = Tk()
root.title("Виселица")
canvas = Canvas(root, width=600, height=600)
canvas.pack()


def but():
    y = 0
    while y < 600:
        x = 0
        while x < 600:
            canvas.create_rectangle(x, y, x + 33, y + 33, fill="white", outline="blue")
            x = x + 33
        y = y + 33


fag = '''Привет, игрок! Сыграем?
Принцип игры
Загадывается слово, пишется первая 
и последняя буква, и отмечаются 
места для остальных букв. '''

canvas.create_text(310, 240, text=fag, fill="purple", font=("Helvetica", "14"))
library = ["виселица", "смартфон", "маргарин", "страница", "микрофон", "мегагерц", "креветка"]


def arr():
    but()
    word = random.choice(library)
    wo = word[1: -1]
    wor = []
    for i in wo:
        wor.append(i)
    a0 = canvas.create_text(282, 40, text=word[0], fill="purple", font=("Helvetica", "18"))
    a1 = canvas.create_text(315, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a2 = canvas.create_text(347, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a3 = canvas.create_text(380, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a4 = canvas.create_text(412, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a5 = canvas.create_text(444, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a6 = canvas.create_text(477, 40, text="_", fill="purple", font=("Helvetica", "18"))
    a7 = canvas.create_text(510, 40, text=word[-1], fill="purple", font=("Helvetica", "18"))
    list1 = [1, 2, 3, 4, 5, 6]
    alphabet = "aбвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    er = []
    win = []

    def a(v):
        ind_alf = alphabet.index(v)
        key = alphabet[ind_alf]

        if v in wor:

            ind = wor.index(v)
            b2 = list1[ind]
            wor[ind] = '1'

            def krd():
                if b2 == 1:
                    x1, y1 = 315, 40
                if b2 == 2:
                    x1, y1 = 347, 40
                if b2 == 3:
                    x1, y1 = 380, 40
                if b2 == 4:
                    x1, y1 = 412, 40
                if b2 == 5:
                    x1, y1 = 444, 40
                if b2 == 6:
                    x1, y1 = 477, 40
                return x1, y1

            x1, y1 = krd()
            win.append(v)
            a2 = canvas.create_text(x1, y1, text=wo[ind], fill="purple", font=("Helvetica", "18"))
            btn[key]["bg"] = "green"
            if v not in wor:
                btn[key]["state"] = "disabled"
            if v in wor:
                win.append(v)
                ind2 = wor.index(v)
                b2 = list1[ind2]
                x1, y1 = krd()
                canvas.create_text(x1, y1, text=wo[ind2], fill="purple", font=("Helvetica", "18"))
            if len(win) == 6:
                canvas.create_text(150, 150, text="Ты победил!", fill="purple", font=("Helvetica", "18"))
                for i in alphabet:
                    btn[i]["state"] = "disabled"
        else:
            er.append(v)
            btn[key]["bg"] = "red"
            btn[key]["state"] = "disabled"

            if len(er) == 1:
                head()

            elif len(er) == 2:
                body()

            elif len(er) == 3:
                arm_r()

            elif len(er) == 4:
                arm_l()

            elif len(er) == 5:
                leg_l()

            elif len(er) == 6:
                leg_r()

                end()
            root.update()
    btn = {}

    def gen(u, x, y):

        btn[u] = Button(root, text=u, width=3, height=1, command=lambda: a(u))
        btn[u].place(x=str(x), y=str(y))
    x = 265
    y = 110
    for i in alphabet[0:8]:
        gen(i, x, y)
        x = x+33
    x = 265
    y = 137
    for i in alphabet[8:16]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 164
    for i in alphabet[16:24]:
        gen(i, x, y)
        x = x + 33
    x = 265
    y = 191
    for i in alphabet[24:33]:
        gen(i, x, y)
        x = x + 33

    def head():
        canvas.create_oval(79, 59, 120, 80, width=4, fill='white')
        root.update()

    def body():
        canvas.create_line(100, 80, 100, 200, width=4)
        root.update()

    def arm_r():
        canvas.create_line(100, 80, 145, 100, width=4)
        root.update()

    def arm_l():
        canvas.create_line(100, 80, 45, 100, width=4)
        root.update()

    def leg_l():
        canvas.create_line(100, 200, 45, 300, width=4)
        root.update()

    def leg_r():
        canvas.create_line(100, 200, 145, 300, width=4)
        root.update()

    def end():
        canvas.create_text(150, 150, text="Ты проиграл", fill="purple", font=("Helvetica", "18"))
        for i in alphabet:
            btn[i]["state"] = "disabled"


btn01 = Button(root, text="Начать игру", width=10, height=1, command=lambda: arr())
btn01.place(x=258, y=442)
btn01["bg"] = "red"

root.mainloop()
