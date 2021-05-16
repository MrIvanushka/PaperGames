from kivy.uix.image import AsyncImage
from kivy.uix.button import Button
# хранилище изображений


def create_button(canvas, gfx, pos):
    play_button = Button()
    play_button.size = gfx.size
    play_button.background_color = (1, 1, 1, 0)
    canvas.add_widget(play_button)
    canvas.add_widget(gfx)
    play_button.pos = gfx.pos = pos
    return play_button

exit_button_gfx = AsyncImage(source='Images/EXITBUTTON.png')
def create_exit_button(canvas, func):
    exit_button = Button()
    exit_button.size = exit_button_gfx.size = (100, 50)
    exit_button.background_color = (1, 1, 1, 0)
    canvas.add_widget(exit_button)
    canvas.add_widget(exit_button_gfx)
    exit_button.pos = exit_button_gfx.pos = (10,540)
    exit_button.bind(on_press=func)

pause_button_source = ['Images/PauseButton.png', 'Images/ResumeButton.png']
def create_pause_button(canvas, func):
    pause_button = Button()
    pause_button_gfx = AsyncImage(source=pause_button_source[0])
    pause_button.size = pause_button_gfx.size = (60, 60)
    pause_button.background_color = (1, 1, 1, 0)
    canvas.add_widget(pause_button)
    canvas.add_widget(pause_button_gfx)
    pause_button.pos = pause_button_gfx.pos = (740,540)
    pause_button.bind(on_press=func)

title = AsyncImage(source='Images/title.png')
title.size = (800, 600)

play_button_gfx = AsyncImage(source='Images/playButton.png')
play_button_gfx.size = (300, 100)

start_button_gfx = AsyncImage(source='Images/Start.png')
start_button_gfx.size = (300, 100)

background = AsyncImage(source='Images/Background.png')
background.size = (800, 600)

viselitsa_start_text = AsyncImage(source='Images/viselitsaStarttext.png')
viselitsa_start_text.size = (600, 400)

menu_page = [AsyncImage(source='Images/viselPage.png'),
             AsyncImage(source='Images/ballsPage.png'),
             AsyncImage(source='Images/pushkaPage.png'),
             AsyncImage(source='Images/starPage.png')]
for page in menu_page:
    page.size = (800, 600)


left_arrow_gfx = AsyncImage(source='Images/leftarrow.png')
right_arrow_gfx = AsyncImage(source='Images/rightarrow.png')
left_arrow_gfx.size = right_arrow_gfx.size = (80, 100)

record_text = AsyncImage(source = 'Images/Record.png')
record_text.size = (300, 80)