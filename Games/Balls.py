from Templates import game
from kivy.uix.image import AsyncImage
from copy import deepcopy

#---------------------------------------необходимые классы--------------------------------------------------------------

class Ball(AsyncImage):
    def __init__(self):

    def move(self, speed):
        self.pos += (0, speed)
    def draw(self, screen):
        # Рисует сам шарик
        circle(screen, self.color, (self.x, self.y), self.r)
        # Рисует блик
        for i in range(self.r):
            circle(screen, [int(c + (255 - c) * i / self.r) for c in self.color],
                   [self.x + int(i / 2), self.y - int(i / 2)], self.r - i)
        # Рисует вереовчку
        lines(screen, BLACK, False, [[self.x, self.y + self.r], [self.x, self.y + 2 * self.r]], 1)
        # Рисует треугольник
        polygon(screen, self.color, [
            (self.x, self.y + self.r),
            (self.x + int(self.r / 10), self.y + self.r + int(self.r / 10)),
            (self.x - int(self.r / 10), self.y + self.r + int(self.r / 10)),
        ])

    def pos_inside(self, pos):
        a = pos[0] - self.x
        b = pos[1] - self.y
        return a ** 2 + b ** 2 < self.r ** 2


def add_ball(self):
    x = randint(int(self.screen_size[0] * 0.1), int(self.screen_size[0] * 0.9))
    y = SCREEN_SIZE[1]
    r = randint(10, max(10, min(self.screen_size) * 0.1))
    color = [randint(0, 255) for _ in range(3)]
    balls.append(Ball(x, y, r, color))

    def draw(self):
        self.screen.fill(WHITE)
        for ball in self.balls:
            ball.change_pos(5 + self.score / 3)
            ball.draw(self.screen)
        self.closeButton.draw(self.screen)
        self.draw_score()
        pygame.display.update()

    def on_click(self, pos):
        if self.closeButton.pos_inside(pos):
            pygame.quit()
            exit(1)
        for ball in self.balls:
            if ball.pos_inside(pos):
                self.balls.remove(ball)
                self.score += 1


#------------------------------------главные исполняющие методы---------------------------------------------------------

class Balls(game):
    def Start(self, canvas):
        # метод для открытия стартовых окон и запуска игры
        # на вход берёт kivy.uix.widget

        pass

    def Update(self, canvas):
        game.draw()
        game.add_ball()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True
            if event.type == pygame.MOUSEBUTTONUP:
                game.on_click(pygame.mouse.get_pos())
        pass

balls = []
score = 0