from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
# хранилище изображений

title = AsyncImage(source='Images/title.png')
title.size = (800, 600)

play_button = Button()
play_button_gfx = AsyncImage(source='Images/playButton.png')
play_button_gfx.size = play_button.size = (300, 100)
play_button.add_widget(play_button_gfx)
play_button.background_color = (0, 0, 0, 0)


background = AsyncImage(source='Images/Background.png')
background.size = (800, 600)
