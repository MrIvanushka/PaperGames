import random
from Templates import game
import GraphicsManager
from kivy.uix.button import Button
from kivy.uix.label import Label

#библиотека слов
library = ["аллергик", "атлетика", "апельсин", "астроном", "активист", "алгоритм", "аргумент", "аэропорт", "булыжник", "больница", "бедность", "бурундук", "биология", "божество",
           "брожение", "вереница", "верхушка", "величина", "виньетка", "винегрет", "виселица", "волейбол", "выскочка", "гусеница", "гипотеза", "гороскоп", "голубика" "грибница",
           "гребешок", "говядина", "горбушка", "глупость", "гирлянда", "горизонт", "движение", "двоечник", "дворняга", "девичник", "дедукция", "дезертир", "действие", "диетолог",
           "делитель", "декольте", "дерзость", "детектив", "диктофон", "директор", "единорог", "живопись",  "жидкость", "инфекция", "изолятор", "индукция", "источник", "иероглиф",
           "институт", "инверсия", "инстинкт", "изоляция", "изолятор", "кинетика", "конспект", "кузнечик", "конфликт", "кормушка", "комиссия", "креветка", "компресс", "костяшка",
           "корзинка", "кондитер", "крокодил", "культура", "косточка", "контроль", "клубника", "легионер", "лексикон", "лестница", "летопись", "лингвист", "мудрость", "молодёжь",
           "монумент", "мерзость", "менеджер", "молочник", "молекула", "мотоцикл", "морковка", "медицина", "микрофон", "ночлежка", "небылица", "небосвод", "отросток", "ответчик",
           "одеколон", "объектив", "оговорка", "обезьяна", "повестка", "переулок", "подборка", "похороны", "покрытие", "перловка", "поясница", "привычка", "пистолет", "пчеловод",
           "подлость", "психолог", "переемник", "политика", "редкость", "рукопись", "режиссёр", "ровесник", "родитель", "сведение", "свекровь", "светофор", "свойство", "сожитель",
           "телескоп", "теоретик", "тепловоз", "теплоход", "терпение", "техникум", "труженик"  "увертюра", "углеводы", "угощение", "униформа", "фокусник", "фельдшер", "фигурист",
           "форточка", "хлебороб", "хождение", "хитрость", "хлопушка", "хоккеист", "хорошист", "холостяк", "художник", "цветовод", "цыпленок", "целитель", "чиновник", "чёрточка",
           "черёмуха", "черновик", "чернозём", "черчение", "четвёрка", "чечевица", "чистовик", "чудовище", "шестёрка", "шнуровка", "шимпанзе", "шиповник", "школьник", "эпидемия",
           "эволюция", "экология", "экспресс", "электрик", "электрод", "электрон", "эпицентр", "эстетика", "этикетка", "эрудиция", "языковед", ]
alphabet = "aбвгдеёжзийклмнопрстуфхцчшщъыьэюя"


#------------------------------------функции игровых механик------------------------------------------------------------

def create_text(canvas, pos, letter):
    label = Label(text=letter, font_size='18sp', color=(0, 0, 1))
    canvas.add_widget(label)
    label.pos = pos


def draw_scene(canvas):
    #выбираем случайным образом слово из библиотеки нашей
    word = random.choice(library)
    wo = word[1: -1]
    word_center = []
    for i in wo:
        word_center.append(i)

    #отрисовываем пустые места для букв
    for i in range(8):
        letter = word[i]
        if (i >= 1) and (i < 7):
            letter = '_'
        create_text(canvas, (220 + i * 25, 490), letter)

    btn = {}
    er = []
    win = []
    list1 = [1, 2, 3, 4, 5, 6]

    def a(v):
        ind_alf = alphabet.index(v)
        key = alphabet[ind_alf]

        # если буква есть в слове, то будем менять ее на 1
        if v in word_center:

            ind = word_center.index(v)
            b2 = list1[ind]
            word_center[ind] = '1'

            #координаты, куда вписываем угаданную букву
            def krd():
                if b2 == 1:
                    x1, y1 = 245, 490
                if b2 == 2:
                    x1, y1 = 270, 490
                if b2 == 3:
                    x1, y1 = 295, 490
                if b2 == 4:
                    x1, y1 = 320, 490
                if b2 == 5:
                    x1, y1 = 345, 490
                if b2 == 6:
                    x1, y1 = 370, 490
                return x1, y1

            x1, y1 = krd()
            win.append(v)
            create_text(canvas, (x1, y1), wo[ind])
            btn[key].background_color = (0, 1, 0, 1)
            #if v not in word_center:
                #btn[key] = "background_disabled_normal"
            if v in word_center:
                win.append(v)
                ind2 = word_center.index(v)
                b2 = list1[ind2]
                x1, y1 = krd()
                create_text(canvas, (x1, y1), wo[ind2])
            #если все буквы угадали
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


    #отрисовка алфавита
    def gen(u, x, y):
        btn[u] = Button(text=u)
        canvas.add_widget(btn[u])
        btn[u].bind(on_press=lambda event: a(u))
        btn[u].pos = (x, y)
        btn[u].size = (20, 20)
    x = 270
    y = 165
    for i in alphabet[0:8]:
        gen(i, x, y)
        x = x + 23
    x = 270
    y = 141
    for i in alphabet[8:16]:
        gen(i, x, y)
        x = x + 23
    x = 270
    y = 118
    for i in alphabet[16:24]:
        gen(i, x, y)
        x = x + 23
    x = 270
    y = 94
    for i in alphabet[24:33]:
        gen(i, x, y)
        x = x + 23
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
    play_button = GraphicsManager.create_button(canvas, GraphicsManager.start_button_gfx, (250, 40))
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
        GraphicsManager.create_exit_button(canvas, lambda event: game.Exit(self, canvas, background, self.UI))

Instance = Visel()