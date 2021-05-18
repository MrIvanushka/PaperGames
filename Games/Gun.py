from Templates import game
import GraphicsManager
from kivy.uix.label import Label
from enum import Enum
from time import time
from random import randint
import math
from kivy.uix.image import AsyncImage
from kivy.uix.widget import Widget
from kivy.graphics import Rotate
from kivy.graphics.context_instructions import PopMatrix, PushMatrix

game_is_started = False

Bullets = []
Targets = []
#----------------------------------------функции игровых механик--------------------------------------------------------


########### пушка и пр.

class BulletType(Enum) :
    casual = 0
    bomb = 1


class Cannon:
    max_velocity = 10
    ChargedBulletType = BulletType.casual
    def __init__(self, canvas):
        self.canvas = canvas
        self.wheels = GraphicsManager.gun_wheels
        self.cannon = GraphicsManager.gun
        self.cannon.rot = Rotate()
        self.cannon.rotate = True
        canvas.add_widget(self.cannon)
        canvas.add_widget(self.wheels)
        self.wheels.pos = (35, 200)
        self.cannon.pos = (40, 230)
        self.direction = 0
        self.cannon.angle = 0
        with self.cannon.canvas.before:
            PushMatrix()
            self.cannon.rot = Rotate()
            self.cannon.rot.axis = (0, 0, 1)
            self.cannon.rot.origin = self.cannon.center
            self.cannon.rot.angle = self.cannon.angle
        with self.cannon.canvas.after:
            PopMatrix()

    def aim(self, x, y):
        """
        Меняет направление direction так, чтобы он из точки
         (self.x, self.y) указывал в точку (x, y).
        :param x: координата x, в которую целимся
        :param y: координата y, в которую целимся
        :return: None
        """
        self.direction = 180 + math.atan2(self.cannon.pos[1] - y, self.cannon.pos[0] - x) / math.pi * 180
        self.cannon.rot.origin = self.wheels.center
        self.cannon.axis = (0, 0, 1)
        self.cannon.rot.angle = self.direction

    def fire(self, power):
        if power > 0.15 and power < 10:
            power *= 300
            v_x = math.cos(self.direction / 180 * math.pi) * power
            v_y = math.sin(self.direction / 180 * math.pi) * power
            x = self.wheels.get_center_x() + 50 * v_x / power
            y = self.wheels.get_center_y() + 50 * v_y / power

            if self.ChargedBulletType == BulletType.bomb:
                shell = Bomb(self.canvas, (x, y), self.wheels.pos[1] - 80, v_x, v_y)
            else:
                shell = Bullet(self.canvas, (x, y), self.wheels.pos[1] - 80, v_x, v_y)
            global Bullets
            Bullets.append(shell)

    def move(self, newPos):
        if newPos > 450:
            newPos = 450
        elif newPos < 100:
            newPos = 100
        self.cannon.rot.angle = 0
        self.wheels.pos = (self.wheels.pos[0], newPos - 30)
        self.cannon.pos = (self.cannon.pos[0], newPos)

########### снаряды

class Bullet(AsyncImage):
    damage = 50
    def __init__(self, canvas, pos, startY, Vx, Vy):
        AsyncImage.__init__(self, source='Images/Bullet.png')
        self.shadow = AsyncImage(source='Images/Bullet.png')
        self.pos = pos
        self.shadow.size = (50, 20)
        self.size = (40, 40)
        self.startY = startY
        print(self.startY)
        self.Vx = Vx
        self.Vy = Vy
        self.is_alive = True
        canvas.add_widget(self)
        canvas.add_widget(self.shadow)

    def move(self, dt):
        self.pos[0] += self.Vx * dt
        self.pos[1] += self.Vy*dt - 90*(dt**2)/2
        self.shadow.pos = (self.pos[0], self.startY)
        self.Vy -= 90*dt
        if self.pos[1] <= self.startY:
            self.is_alive = False

    def detect_collision(self):
        if  self.pos[1] - self.startY < 35:
            for target in Targets:
                if(target.IsInRange(self.pos[0] + 25,self.pos[1] + 25, 20)):
                    target.GetDamage(self.damage)
                    print("HIT!")

    def delete(self, canvas):
        canvas.remove_widget(self.shadow)
        canvas.remove_widget(self)


class Bomb (Bullet):
    damage = 8

    def detect_collision(self, other):
        if self.startY - self.y < 5:
            for target in other:
                if(target.IsInRange(self.x + 10,self.y + 10, 150)):
                    target.GetDamage(self.damage)
                    print("HIT!")


class ClickableBackground(Widget):
    def __init__(self, cannon):
        Widget.__init__(self)
        self.size = (800, 600)
        self.cannon = cannon
        self.fire_power = -1

    def on_touch_move(self, touch):
        if touch.pos[0] < 100 and game_is_started:
            self.cannon.move(touch.pos[1])
        else:
            self.cannon.aim(touch.pos[0], touch.pos[1])
            if self.fire_power < 0:
                self.fire_power = time()

    def on_touch_down(self, touch):
        if touch.pos[0] > 100 and game_is_started:
            self.cannon.aim(touch.pos[0], touch.pos[1])
            self.fire_power = time()

    def on_touch_up(self, touch):
        if touch.pos[0] > 100 and game_is_started:
            self.cannon.fire(time() - self.fire_power)
            self.fire_power = -1

########## враги

class Target(AsyncImage):
    def __init__(self, canvas):
        i = randint(0, 100) % 3
        AsyncImage.__init__(self, source=GraphicsManager.skeleton_source[i])
        self.size = GraphicsManager.skeleton_size[i]
        self.pos = (randint(750, 850), randint(100, 400))
        self.is_alive = True
        self.hp = 10
        self.Vx = 6
        canvas.add_widget(self)

    def move(self, dt):
        """
        Сдвигает шарик-мишень исходя из его кинематических характеристик
        и длины кванта времени dt
        в новое положение, а также меняет его скорость.
        :param dt:
            :return:
        """
        self.x -= self.Vx * dt

    def IsInRange(self, x, y, range):
        if math.fabs(self.center_x - x) < range and math.fabs(self.pos[1] + 20 - y) < range:
            return True
        return False

    def GetDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.is_alive = False

#------------------------------------главные исполняющие методы---------------------------------------------------------

class Gun(game):
    def start_game(self):
        # закрывает стартовое окно и начинает игру
        self.background.clear_widgets()
        global game_is_started
        game_is_started = True
        GraphicsManager.create_pause_button(self.background, lambda event: self.pause())
        self.record = 0
        self.score = -1
        self.raise_score()
        self.background.add_widget(self.score_label)
        self.score_label.pos = (100, 500)
        self.cannon = Cannon(self.background)
        self.background.add_widget(ClickableBackground(self.cannon))

    def pause(self):
        print("paused")
        global game_is_started
        if game_is_started:
            game_is_started = False
        else:
            game_is_started = True

    def raise_score(self):
        self.score += 1
        self.score_label.text = '[i]' + str(self.score) + '[/i]'


    def create_startmessage(self):
        start_button = GraphicsManager.create_button(self.background, GraphicsManager.start_button_gfx, (250, 180))
        start_button.bind(on_press=lambda event: self.start_game())
        RT = GraphicsManager.record_text
        self.background.add_widget(RT)
        self.background.add_widget(self.record_label)
        self.record_label.pos = (500, 300)
        RT.pos = (200, 310)
        self.frame_time = time()
        self.spawn_delay_time = time()

    def stop(self):
        global game_is_started
        game_is_started = False
        self.background.clear_widgets()
        self.create_startmessage()
        if self.score > self.record:
            self.record = self.score
            self.record_label.text = '[i]' + str(self.record) + '[/i]'
        self.background.add_widget(self.score_label)
        self.score_label.text = text='[i] Счёт: ' + str(self.score) + '[/i]'
        self.score_label.pos = (300, 410)


    def Start(self, canvas):
        self.score_label = Label(text='[i]' + str(0) + '[/i]', font_size='90sp', color=(0, 0, 0.5), markup=True)
        self.record_label = Label(text='[i]' + str(0) + '[/i]', font_size='90sp', color=(0, 0, 0.5), markup=True)
        canvas.clear_widgets()
        self.background = GraphicsManager.gun_background
        canvas.add_widget(self.background)
        GraphicsManager.create_exit_button(canvas, lambda event: game.Exit(self, canvas, self.background))
        self.create_startmessage()
        self.spawn_delay = 3

    def Update(self, canvas):
        if game_is_started:
            if time() - self.spawn_delay_time > self.spawn_delay:
                Targets.append(Target(self.background))
                print("Spawning mob...")
                self.spawn_delay -= 0.01
                self.spawn_delay_time = time()

            for target in Targets:
                target.move(time()-self.frame_time)
                if target.is_alive == False:
                    self.background.remove_widget(target)
                    Targets.remove(target)

            for bullet in Bullets:
                bullet.move(time()-self.frame_time)
                bullet.detect_collision()
                if bullet.is_alive == False:
                    bullet.delete(self.background)
                    Bullets.remove(bullet)
        self.frame_time = time()


Instance = Gun()