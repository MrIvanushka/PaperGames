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
        self.ChargedBulletType = BulletType.casual
        with self.cannon.canvas.before:
            PushMatrix()
            self.cannon.rot = Rotate()
            self.cannon.rot.axis = (0, 0, 1)
            self.cannon.rot.origin = self.cannon.center
            self.cannon.rot.angle = self.cannon.angle
        with self.cannon.canvas.after:
            PopMatrix()
        Instance.weapon_button.bind(on_press=lambda event: self.change_bullet())

    def change_bullet(self):
        if self.ChargedBulletType == BulletType.casual:
            self.ChargedBulletType = BulletType.bomb
            Instance.current_weapon.source = 'Images/Bomb.png'
        else:
            self.ChargedBulletType = BulletType.casual
            Instance.current_weapon.source = 'Images/Bullet.png'

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
                shell = Bomb(self.canvas, (x, y), self.wheels.pos[1] - 50, v_x, v_y)
            else:
                shell = Bullet(self.canvas, (x, y), self.wheels.pos[1] - 50, v_x, v_y)
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
    def __init__(self, canvas, pos, startY, Vx, Vy):
        AsyncImage.__init__(self, source='Images/Bullet.png')
        self.range = 20
        self.create_gfx(canvas, pos, startY, 20, Vx, Vy)


    def create_gfx(self, canvas, pos, startY, damage, Vx, Vy):
        self.shadow = AsyncImage(source='Images/Shadow.png')
        self.pos = pos
        self.shadow.size = (40, 20)
        self.size = (40, 40)
        self.startY = startY
        self.damage = damage
        print(self.startY)
        self.Vx = Vx
        self.Vy = Vy
        self.is_alive = True
        canvas.add_widget(self.shadow)
        canvas.add_widget(self)


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
                if(target.IsInRange(self.pos[0] + 25, self.pos[1] + 25, self.range)):
                    target.GetDamage(self.damage)
                    self.is_alive = False
                    print("HIT!")

    def delete(self, canvas):
        canvas.remove_widget(self.shadow)
        canvas.remove_widget(self)


class Bomb (Bullet):
    def __init__(self, canvas, pos, startY, Vx, Vy):
        AsyncImage.__init__(self, source='Images/Bomb.png')
        self.range = 80
        self.create_gfx(canvas, pos, startY, 8, Vx, Vy)



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
        source = GraphicsManager.skeleton_source[i]
        self.create_character(canvas, source, 10, 10, 3)
        self.size = GraphicsManager.skeleton_size[i]
        self.pos = (randint(750, 850), randint(100, 400))


    def create_character(self, canvas, _source, Vx, hp, damage):
        AsyncImage.__init__(self, source=_source)
        self.is_alive = True
        self.damage = 3
        self.hp = hp
        self.Vx = Vx
        canvas.add_widget(self)

    def move(self, dt):
        self.x -= self.Vx * dt
        if self.x < 150:
            Instance.take_damage(self.damage)
            self.is_alive = False

    def IsInRange(self, x, y, range):
        if math.fabs(self.center_x - x) < range and (math.fabs(self.center_y - y - 20) < self.size[1]/2 or math.fabs(self.center_y - y) < range):
            return True
        return False

    def GetDamage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.is_alive = False
            Instance.raise_score()

class Boss(Target):
    def __init__(self, canvas):
        i = randint(0, 100) % 3
        self.create_character(canvas, GraphicsManager.boss,  3, 200, 20)
        self.size = (90, 180)
        self.pos = (randint(750, 850), randint(100, 400))
        print("BOSS IS SPAWNED!")

#------------------------------------главные исполняющие методы---------------------------------------------------------

class Gun(game):
    def start_game(self):
        # закрывает стартовое окно и начинает игру
        self.weapon_button = GraphicsManager.create_button(self.UI, GraphicsManager.gun_corner, (10, 10))
        self.current_weapon = AsyncImage(source = 'Images/Bullet.png')
        self.current_weapon.size = (80,80)
        self.current_weapon.pos = (20, 20)
        self.UI.add_widget(self.current_weapon)
        self.background.clear_widgets()
        global game_is_started
        game_is_started = True
        GraphicsManager.create_pause_button(self.background, lambda event: self.pause())
        self.record = 0
        self.score = -1
        self.raise_score()
        self.background.add_widget(self.score_label)
        self.score_label.pos = (650, 10)
        self.cannon = Cannon(self.background)
        self.background.add_widget(ClickableBackground(self.cannon))
        self.HP = 100
        HC = GraphicsManager.HP_corners
        self.hitbar_gfx = GraphicsManager.Hitbar
        self.UI.add_widget(HC)
        self.UI.add_widget(self.hitbar_gfx)
        HC.pos = (190, 530)
        self.hitbar_gfx.pos = (200, 530)
        self.boss_value = 15


    def take_damage(self, damage):
        self.HP -= damage
        self.hitbar_gfx.size[0] = 480 * (self.HP / 100)
        if self.HP <= 0:
            self.stop()

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
        canvas.add_widget(self.UI)
        GraphicsManager.create_exit_button(canvas, lambda event: game.Exit(self, canvas, self.background, self.UI))
        self.create_startmessage()
        self.spawn_delay = 3


    def Update(self, canvas):
        if game_is_started:
            if time() - self.spawn_delay_time > self.spawn_delay:
                Targets.append(Target(self.background))
                print("Spawning mob...")
                if self.spawn_delay > 0.02:
                    self.spawn_delay -= 0.01
                self.spawn_delay_time = time()

            if self.score > self.boss_value:
                Targets.append(Boss(self.background))
                self.boss_value += 50

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