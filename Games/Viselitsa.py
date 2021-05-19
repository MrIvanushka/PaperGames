import random
from Templates import game
import GraphicsManager
from kivy.uix.button import Button
from kivy.uix.label import Label

# библиотека слов
library = ["аллергик", "атлетика", "апельсин", "астроном", "активист", "алгоритм", "аргумент", "аэропорт", "булыжник",
           "больница", "бедность", "бурундук", "биология", "божество", "брожение", "вереница", "верхушка", "величина",
           "виньетка", "винегрет", "виселица", "волейбол", "выскочка", "гусеница", "гипотеза", "гороскоп", "голубика" 
           "грибница", "гребешок", "говядина", "горбушка", "глупость", "гирлянда", "горизонт", "движение", "двоечник",
           "дворняга", "девичник", "дедукция", "дезертир", "действие", "диетолог", "делитель", "декольте", "дерзость",
           "детектив", "диктофон", "директор", "единорог", "живопись",  "жидкость", "инфекция", "изолятор", "индукция",
           "источник", "иероглиф", "институт", "инверсия", "инстинкт", "изоляция", "изолятор", "кинетика", "конспект",
           "кузнечик", "конфликт", "кормушка", "комиссия", "креветка", "компресс", "костяшка", "корзинка", "кондитер",
           "крокодил", "культура", "косточка", "контроль", "клубника", "легионер", "лексикон", "лестница", "летопись",
           "лингвист", "мудрость", "молодёжь", "монумент", "мерзость", "менеджер", "молочник", "молекула", "мотоцикл",
           "морковка", "медицина", "микрофон", "ночлежка", "небылица", "небосвод", "отросток", "ответчик", "одеколон",
           "объектив", "оговорка", "обезьяна", "повестка", "переулок", "подборка", "похороны", "покрытие", "перловка",
           "поясница", "привычка", "пистолет", "пчеловод", "подлость", "психолог", "переемник", "политика", "редкость",
           "рукопись", "режиссёр", "ровесник", "родитель", "сведение", "свекровь", "светофор", "свойство", "сожитель",
           "телескоп", "теоретик", "тепловоз", "теплоход", "терпение", "техникум", "труженик"  "увертюра", "углеводы",
           "угощение", "униформа", "фокусник", "фельдшер", "фигурист", "форточка", "хлебороб", "хождение", "хитрость",
           "хлопушка", "хоккеист", "хорошист", "холостяк", "художник", "цветовод", "цыпленок", "целитель", "чиновник",
           "чёрточка", "черёмуха", "черновик", "чернозём", "черчение", "четвёрка", "чечевица", "чистовик", "чудовище",
           "шестёрка", "шнуровка", "шимпанзе", "шиповник", "школьник", "эпидемия", "эволюция", "экология", "экспресс",
           "электрик", "электрод", "электрон", "эпицентр", "эстетика", "этикетка", "эрудиция", "языковед"]
alphabet = "aбвгдеёжзийклмнопрстуфхцчшщъыьэюя"


# функции игровых механик

def create_text(canvas, pos, letter):
    label = Label(text=letter, font_size='30sp', color=(0, 0, 1))
    canvas.add_widget(label)
    label.pos = pos


def draw_scene(canvas):
    # рисуем виселицу на фоне
    _visel = GraphicsManager.visel
    canvas.add_widget(_visel)
    _visel.pos = (5, 115)

    # выбираем случайным образом слово из библиотеки нашей
    word = random.choice(library)
    wo = word[1: -1]
    word_center = []
    for i in wo:
        word_center.append(i)

    # отрисовываем пустые места для букв
    for i in range(8):
        letter = word[i]
        if (i >= 1) and (i < 7):
            letter = '_'
        create_text(canvas, (390 + i * 25, 490), letter)

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

            # координаты, куда вписываем угаданную букву
            def krd():
                if b2 == 1:
                    x1, y1 = 415, 490
                if b2 == 2:
                    x1, y1 = 440, 490
                if b2 == 3:
                    x1, y1 = 465, 490
                if b2 == 4:
                    x1, y1 = 490, 490
                if b2 == 5:
                    x1, y1 = 515, 490
                if b2 == 6:
                    x1, y1 = 540, 490
                return x1, y1

            x1, y1 = krd()
            win.append(v)
            create_text(canvas, (x1, y1), wo[ind])
            btn[key].background_color = (0, 1, 0, 1)
            if v in word_center:
                win.append(v)
                ind2 = word_center.index(v)
                b2 = list1[ind2]
                x1, y1 = krd()
                create_text(canvas, (x1, y1), wo[ind2])
            # если все буквы угадали
            if len(win) == 6:
                pass
                create_text(canvas, (500, 355), 'Ты победил!')
                play_button = GraphicsManager.create_button(canvas, GraphicsManager.one_more_button_gfx, (480, 300))
                play_button.bind(on_press=lambda event: Instance.stop())
        else:
            er.append(v)
            btn[key].background_color = (1, 0, 0, 1)
            _body = GraphicsManager.visel_body[len(er)-1]
            canvas.add_widget(_body)
            if len(er) == 1:
                head(_body)

            elif len(er) == 2:
                body(_body)

            elif len(er) == 3:
                #Instance.stop()
                arm_r(_body)

            elif len(er) == 4:
                arm_l(_body)

            elif len(er) == 5:
                leg_l(_body)

            elif len(er) == 6:
                leg_r(_body)

                end()

    # отрисовка алфавита

    def gen(u, x, y):
        btn[u] = Button(text=u)
        canvas.add_widget(btn[u])
        btn[u].bind(on_press=lambda event: a(u))
        btn[u].pos = (x, y)
        btn[u].size = (40, 40)
    x = 365
    y = 233
    for i in alphabet[0:8]:
        gen(i, x, y)
        x = x + 47
    x = 365
    y = 186
    for i in alphabet[8:16]:
        gen(i, x, y)
        x = x + 47
    x = 365
    y = 140
    for i in alphabet[16:24]:
        gen(i, x, y)
        x = x + 47
    x = 365
    y = 94
    for i in alphabet[24:33]:
        gen(i, x, y)
        x = x + 47

    def head(body):
        body.pos = (245, 345)
        pass

    def body(_body):
        _body.pos = (245, 256)
        pass

    def arm_r(body):
        body.pos = (230, 298)
        pass

    def arm_l(body):
        body.pos = (270, 280)
        pass

    def leg_l(body):
        body.pos = (237, 210)
        pass

    def leg_r(body):
        body.pos = (262, 210)
        pass

    def end():
        create_text(canvas, (500, 355), 'Ты проиграл')
        play_button = GraphicsManager.create_button(canvas, GraphicsManager.one_more_button_gfx, (480, 300))
        play_button.bind(on_press=lambda event: Instance.stop())


def set_startmessage(canvas):
    # выводит стартовое сообщение fag на экран.
    # на вход принимает kivy.uix.widget
    st = GraphicsManager.viselitsa_start_text
    canvas.add_widget(st)
    st.pos = (100, 160)
    play_button = GraphicsManager.create_button(canvas, GraphicsManager.start_button_gfx, (250, 40))
    play_button.bind(on_press=lambda event: close_startmessage(canvas))


def close_startmessage(canvas):
    # для закрытия стартового сообщения по нажатии на кнопку
    # на вход принимает kivy.uix.widget
    print("closing startmessage...")
    canvas.clear_widgets()
    draw_scene(canvas)

# главные исполняющие методы


class Visel(game):
    def stop(self):
        close_startmessage(self.background)

    def Start(self, canvas):
        # метод для открытия стартовых окон и запуска игры
        # на вход берёт kivy.uix.widget
        canvas.clear_widgets()
        self.background = GraphicsManager.background
        canvas.add_widget(self.background)
        set_startmessage(self.background)
        GraphicsManager.create_exit_button(canvas, lambda event: game.Exit(self, canvas, self.background, self.UI))


Instance = Visel()
