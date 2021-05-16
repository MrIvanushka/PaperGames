import random
from Templates import game
import GraphicsManager
from kivy.uix.button import Button
from kivy.uix.label import Label

library = ["виселица", "смартфон", "маргарин", "страница", "микрофон", "мегагерц", "креветка"]
alphabet = "aбвгдеёжзийклмнопрстуфхцчшщъыьэюя"


#------------------------------------функции игровых механик------------------------------------------------------------

def create_text(canvas, pos, letter):
    label = Label(text=letter, font_size='18sp', color=(0, 0, 1))
    canvas.add_widget(label)
    label.pos = pos

def draw_scene(canvas):
    #отрисовка всего
    word = random.choice(library)
    wo = word[1: -1]
    word_center = []
    for i in wo:
        word_center.append(i)

    for i in range(8):
        letter = word[i]
        if (i >= 1) and (i < 7):
            letter = '_'
        create_text(canvas, (282 + i * 33, 500), letter)

    btn = {}
    er = []
    win = []
    list1 = [1,2,3,4,5,6]

    def a(v):
        ind_alf = alphabet.index(v)
        key = alphabet[ind_alf]

        if v in word_center:

            ind = word_center.index(v)
            b2 = list1[ind]
            word_center[ind] = '1'

            def krd():
                if b2 == 1:
                    x1, y1 = 315, 500
                if b2 == 2:
                    x1, y1 = 347, 500
                if b2 == 3:
                    x1, y1 = 380, 500
                if b2 == 4:
                    x1, y1 = 412, 500
                if b2 == 5:
                    x1, y1 = 444, 500
                if b2 == 6:
                    x1, y1 = 477, 500
                return x1, y1

            x1, y1 = krd()
            win.append(v)
            create_text(canvas, (x1, y1), wo[ind])
            btn[key].background_color = (0, 1, 0, 1)
            #if v not in word_center:
                #btn[key]["state"] = "disabled"
            if v in word_center:
                win.append(v)
                ind2 = word_center.index(v)
                b2 = list1[ind2]
                x1, y1 = krd()
                create_text(canvas, (x1, y1), wo[ind2])
            if len(win) == 6:
                pass
                create_text(canvas, (150, 150), 'Ты победил!')
                #for i in alphabet:
                    #btn[i]["state"] = "disabled"
        else:
            er.append(v)
            btn[key].background_color = (1, 0, 0, 1)
            #btn[key]["state"] = "disabled"
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


    def gen(u, x, y):
        btn[u] = Button(text=u)
        canvas.add_widget(btn[u])
        btn[u].bind(on_press=lambda event: a(u))
        btn[u].pos = (x, y)
        btn[u].size = (15,15)
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
        #canvas.create_oval(79, 59, 120, 80, width=4, fill='white')
        pass
    def body():
        #canvas.create_line(100, 80, 100, 200, width=4)
        pass
    def arm_r():
        #canvas.create_line(100, 80, 145, 100, width=4)
        pass
    def arm_l():
        #canvas.create_line(100, 80, 45, 100, width=4)
        pass
    def leg_l():
        #canvas.create_line(100, 200, 45, 300, width=4)
        pass
    def leg_r():
        #canvas.create_line(100, 200, 145, 300, width=4)
        pass
    def end():
        create_text(canvas, (150, 150), 'Ты проиграл')
        #for i in alphabet:
            #btn[i]["state"] = "disabled"


def set_startmessage(canvas):
    # выводит стартовое сообщение fag на экран.
    # на вход принимает kivy.uix.widget
    st = GraphicsManager.viselitsa_start_text
    canvas.add_widget(st)
    st.pos = (100, 160)
    play_button = GraphicsManager.create_button(canvas, GraphicsManager.play_button_gfx, (250, 40))
    play_button.bind(on_press=lambda event:close_startmessage(canvas))


def close_startmessage(canvas):
    # для закрытия стартового сообщения по нажатии на кнопку
    # на вход принимает kivy.uix.widget
    print("closing startmessage...")
    canvas.clear_widgets()
    draw_scene(canvas)

#------------------------------------главные исполняющие методы---------------------------------------------------------

class Visel(game):
    def Start(self, canvas):
        # метод для открытия стартовых окон и запуска игры
        # на вход берёт kivy.uix.widget
        canvas.clear_widgets()
        background = GraphicsManager.background
        canvas.add_widget(background)
        set_startmessage(background)
        GraphicsManager.create_exit_button(canvas, lambda event: game.Exit(self, canvas, background))

Instance = Visel()