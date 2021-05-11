import ImageManager
import Templates


def close_game():
    pass


class mainMenu(Templates.game):
    def Start(self, canvas):
        canvas.delete("all")
        canvas.create_image(ImageManager.MainMenu[0])

    def Update(self, canvas):
        pass


Instance = mainMenu()