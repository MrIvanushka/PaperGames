# Родительский класс для всяких там игр которые включаем.

try_to_exit = False

class game:
    def __init__(self):
        self.paused = False
        self.try_to_exit = False

    def Start(self, canvas):
        # метод для открытия стартовых окон и запуска игры
        # на вход берёт kivy.uix.widget
        pass

    def Update(self, canvas):
        # метод для покадрового обновления экрана
        # на вход берёт kivy.uix.widget
        pass

    def Exit(self, canvas, background):
        # метод для выхода из игры, активируется кнопкой
        background.clear_widgets()
        canvas.clear_widgets()
        global try_to_exit
        try_to_exit = True



