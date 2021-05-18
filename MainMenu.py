import GraphicsManager
from Templates import game
from kivy.uix.button import Button
from Games.Viselitsa import Instance as viselitsa
from Games.Gun import Instance as gun
from Games.Balls import Instance as balls

#------------------------------------------------наследование-----------------------------------------------------------


class mainMenu(game):

    def Start(self, canvas):
        # метод для открытия стартовых окон и запуска игры
        # на вход берёт kivy.uix.widget
        self.currentGame = Instance
        self.current_page = 0
        print("Mainmenu is running")
        canvas.clear_widgets()
        canvas.add_widget(GraphicsManager.title)
        play_button = GraphicsManager.create_button(canvas, GraphicsManager.play_button_gfx, (250, 40))
        play_button.bind(on_press=lambda event: self.open_page_list(canvas))
        print("Canvas was overwritten")
    #canvas.add_widget(GraphicsManager.play_button)

    def open_page_list(self, canvas):
        # открытие страниц меню
        # на вход берёт kivy.uix.widget
        print("opening page list...")
        canvas.clear_widgets()
        canvas.add_widget(GraphicsManager.background)
        play_button = Button()
        play_button.size = (640, 380)
        play_button.background_color = (1, 1, 1, 0)
        canvas.add_widget(play_button)
        play_button.pos = (80, 65)
        play_button.bind(on_press=lambda event: self.load_game(canvas))
        left_arrow = GraphicsManager.create_button(canvas, GraphicsManager.left_arrow_gfx, (0, 200))
        right_arrow = GraphicsManager.create_button(canvas, GraphicsManager.right_arrow_gfx, (720, 200))
        left_arrow.bind(on_press=lambda event: self.open_page(canvas, -1))
        right_arrow.bind(on_press=lambda event: self.open_page(canvas, 1))
        self.open_page(canvas, 0)

    def open_page(self, canvas, page):
        # сменяет !!открытую!! страницу на новую
        # на вход берёт kivy.uix.widget и int направление новой страницы
        if page != 0:
            self.current_page += page
            canvas.remove_widget(self.menu_gfx)
        else:
            self.current_page = 0
        print(self.current_page)
        if self.current_page >= len(game_list):
            self.current_page = 0
        elif self.current_page < 0:
            self.current_page = len(game_list) - 1

        self.menu_gfx = GraphicsManager.menu_page[self.current_page]
        canvas.add_widget(self.menu_gfx)

    def load_game(self, canvas):
        # запускает игру, показанную на данной странице
        # на вход берёт kivy.uix.widget
        self.currentGame = game_list[self.current_page]
        self.currentGame.Start(canvas)




Instance = mainMenu()
game_list = [viselitsa, balls, gun]
