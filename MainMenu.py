import GraphicsManager
from Templates import game
from Games.Viselitsa import Instance as viselitsa
from kivy.uix.button import Button
#-----------------------------------------------всякие функции----------------------------------------------------------


def open_page_list(canvas):
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
    play_button.bind(on_press=lambda event: load_game(canvas))
    open_page(canvas, 0)

def open_page(canvas, page):
    # сменяет !!открытую!! страницу на новую
    # на вход берёт kivy.uix.widget и новую страницу
    global current_page
    current_page = page
    if current_page >= len(game_list):
        current_page = 0
    elif current_page < 0:
        current_page = len(game_list) - 1
    canvas.add_widget(GraphicsManager.menu_page[page])

def load_game(canvas):
    # запускает игру, показанную на данной странице
    # на вход берёт kivy.uix.widget
    currentGame = game_list[current_page]
    currentGame.Start(canvas)

#------------------------------------------------наследование-----------------------------------------------------------


class mainMenu(game):
    def Start(self, canvas):
        # метод для открытия стартовых окон и запуска игры
        # на вход берёт kivy.uix.widget
        global currentGame
        currentGame = Instance
        print("Mainmenu is running")
        canvas.clear_widgets()
        canvas.add_widget(GraphicsManager.title)
        play_button = GraphicsManager.create_button(canvas, GraphicsManager.play_button_gfx, (250, 40))
        play_button.bind(on_press=lambda event: open_page_list(canvas))
        print("Canvas was overwritten")
    #canvas.add_widget(GraphicsManager.play_button)


Instance = mainMenu()
currentGame = Instance
game_list = [viselitsa]
current_page = 0