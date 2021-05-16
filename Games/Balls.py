from Templates import game
from kivy.uix.image import AsyncImage
import GraphicsManager
from random import randint
import time

#----------------------------------------функции игровых механик--------------------------------------------------------

class Ball(AsyncImage):
    def __init__(self, x, scale):
        AsyncImage.__init__(self)
        self.source ='Images/Ball.png'
        self.pos = (x, -30)
        self.size = (scale, scale * 17/12)

    def move(self, speed):
        self.pos = (self.pos[0], self.pos[1]+speed)


    def pos_inside(self, pos):
        a = pos[0] - self.x
        b = pos[1] - self.y
        return a ** 2 + b ** 2 < self.r ** 2


    def on_click(self, pos):
        for ball in self.balls:
            if ball.pos_inside(pos):
                self.balls.remove(ball)
                self.score += 1


#------------------------------------главные исполняющие методы---------------------------------------------------------

class Balls(game):
    def add_ball(self):
        x = randint(0, 740)
        scale = randint(50, 150)
        new_ball = Ball(x, scale)
        self.background.add_widget(new_ball)
        self.balls.append(new_ball)

    def Start(self, canvas):
        # метод для открытия стартовых окон и запуска игры
        # на вход берёт kivy.uix.widget
        canvas.clear_widgets()
        self.background = GraphicsManager.background
        canvas.add_widget(self.background)
        GraphicsManager.create_exit_button(canvas, lambda event: game.Exit(self, canvas, self.background))
        self.balls = []
        self.current_time = time.time()
        self.time_delay = 0.5
        self.ball_speed = 1
        pass

    def Update(self, canvas):
        if time.time() - self.current_time > self.time_delay:
            self.current_time = time.time()
            self.add_ball()
        for ball in self.balls:
            ball.move(self.ball_speed)

Instance = Balls()
balls = []
score = 0