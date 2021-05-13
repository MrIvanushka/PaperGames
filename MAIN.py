from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.clock import Clock
from MainMenu import Instance as mainMenu
from MainMenu import currentGame
# собсна главный скрипт: инициализация окна и вызов команд обновления классов

#---------------------------------------классы и наследование-----------------------------------------------------------

class BaseApp(App):
    def build(self):
        self.canvas = Widget()
        mainMenu.Start(self.canvas)
        Clock.schedule_interval(self.update, 0.01)
        return self.canvas

    def update(self, *args):
        currentGame.Update(self.root)
        Clock.unschedule(self.update)
        Clock.schedule_interval(self.update, 0.01)


#-----------------------------------------инициализация окна------------------------------------------------------------


Window.size = (800, 600)
ThisApp = BaseApp()
ThisApp.run()
ThisApp.update()
