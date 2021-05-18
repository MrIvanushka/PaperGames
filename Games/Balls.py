from Templates import game
from kivy.uix.image import AsyncImage
from kivy.uix.label import Label
import GraphicsManager
from random import randint
import time

#----------------------------------------функции игровых механик--------------------------------------------------------

game_is_started = False

class Ball(AsyncImage):
    def __init__(self, x, scale):
        AsyncImage.__init__(self)
        self.source ='Images/Ball.png'
        self.pos = (x, -30)
        self.size = (scale, scale * 17/12)

    def move(self, speed):
        self.pos = (self.pos[0], self.pos[1]+speed)


    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos) and game_is_started:
            self.parent.remove_widget(self)
            global Instance
            Instance.raise_score()

#------------------------------------главные исполняющие методы---------------------------------------------------------

class Balls(game):
    def add_ball(self):
        # спаунит новый шарик
        x = randint(0, 740)
        scale = randint(50, 150)
        new_ball = Ball(x, scale)
        self.background.add_widget(new_ball)
        self.balls.append(new_ball)

    def start_game(self):
        # закрывает стартовое окно и начинает игру
        self.background.clear_widgets()
        global game_is_started
        game_is_started = True
        GraphicsManager.create_pause_button(self.UI, lambda event: self.pause())
        self.remaining_time = 20.0
        self.balls = []
        self.time_delay = 0.5
        self.ball_speed = 1
        self.score = -1
        self.raise_score()
        self.UI.add_widget(self.score_label)
        self.score_label.pos = (100, 500)
        self.UI.add_widget(self.countdown_label)
        self.countdown_label.pos = (600,500)

    def pause(self):
        global game_is_started
        if game_is_started:
            game_is_started = False
        else:
            game_is_started = True

    def raise_score(self):
        self.score += 1
        self.score_label.text = '[i]' + str(self.score) + '[/i]'
        self.ball_speed += 0.1


    def create_startmessage(self):
        start_button = GraphicsManager.create_button(self.background, GraphicsManager.start_button_gfx, (250, 180))
        start_button.bind(on_press=lambda event: self.start_game())
        RT = GraphicsManager.record_text
        self.background.add_widget(RT)
        self.background.add_widget(self.record_label)
        self.record_label.pos = (500, 300)
        RT.pos = (200, 310)

    def stop(self):
        global game_is_started
        game_is_started = False
        self.UI.clear_widgets()
        self.background.clear_widgets()
        self.create_startmessage()
        if self.score > self.record:
            self.record = self.score
            self.record_label.text = '[i]' + str(self.record) + '[/i]'
        self.background.add_widget(self.score_label)
        self.score_label.text = text='[i] Счёт: ' + str(self.score) + '[/i]'
        self.score_label.pos = (300, 410)


    def Start(self, canvas):
        # метод для открытия стартовых окон и запуска игры
        # на вход берёт kivy.uix.widget
        self.score_label = Label(text='[i]' + str(0) + '[/i]', font_size='90sp', color=(0, 0, 0.5), markup=True)
        self.record_label = Label(text='[i]' + str(0) + '[/i]', font_size='90sp', color=(0, 0, 0.5), markup=True)
        self.countdown_label = Label(text='[i]' + str(60) + '[/i]', font_size='90sp', color=(0, 0, 0.5),
                                  markup=True)
        self.record = 0
        global game_is_started
        game_is_started = False
        canvas.clear_widgets()
        canvas.add_widget(self.background)
        canvas.add_widget(self.UI)
        GraphicsManager.create_exit_button(canvas, lambda event: game.Exit(self, canvas, self.background, self.UI))
        self.create_startmessage()
        self.current_time = time.time()

    def Update(self, canvas):
        if game_is_started:
            if time.time() - self.current_time > self.time_delay:
                self.remaining_time -= self.time_delay
                self.countdown_label.text = '[i]' + str(int(self.remaining_time)) + '[/i]'
                if self.remaining_time < 0:
                    self.stop()
                self.current_time = time.time()
                self.add_ball()
            for ball in self.balls:
                ball.move(self.ball_speed)


Instance = Balls()
balls = []
score = 0