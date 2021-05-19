from kivy.uix.image import AsyncImage, Image
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
    pause_button.size = pause_button_gfx.size = (70, 70)
    pause_button.background_color = (1, 1, 1, 0)
    canvas.add_widget(pause_button)
    canvas.add_widget(pause_button_gfx)
    pause_button.pos = pause_button_gfx.pos = (720,520)
    pause_button.bind(on_press=func)

title = AsyncImage(source='Images/title.png')
title.size = (800, 600)

play_button_gfx = AsyncImage(source='Images/playButton.png')
play_button_gfx.size = (300, 100)

start_button_gfx = AsyncImage(source='Images/Start.png')
start_button_gfx.size = (300, 100)

background = AsyncImage(source='Images/Background.png')
background.size = (800, 600)


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

gun_background = AsyncImage(source = 'Images/pushka_background.png')
gun_background.size = (800, 600)

gun = AsyncImage(source = 'Images/gun.png')
gun_wheels = AsyncImage(source = 'Images/gunWheels.png')
gun_wheels.size = (80, 80)
gun.size = (150,60)

skeleton_source = ['Images/skeleton1.png',
             'Images/skeleton2.png',
             'Images/skeleton3.png']
boss = 'Images/SkeletonBoss.png'
skeleton_size = [(50, 100), (50, 100), [50, 125]]

HP_corners = AsyncImage(source = 'Images/HP.png')
HP_corners.size = (500, 40)
Hitbar = Button()
Hitbar.background_color = (0, 0, 1, 0.5)
Hitbar.size = (480, 35)

gun_corner = AsyncImage(source = 'Images/Corner.png')
gun_corner.size = (100, 100)

viselitsa_start_text = AsyncImage(source='Images/viselitsaStarttext.png')
viselitsa_start_text.size = (600, 400)

visel_body = [AsyncImage(source='Images/head.png'), AsyncImage(source='Images/body.png'),
              AsyncImage(source='Images/arm_l.png'), AsyncImage(source='Images/arm_r.png'),
              AsyncImage(source='Images/leg_l.png'), AsyncImage(source='Images/leg_r.png')]
visel_body[0].size = (70, 70)
visel_body[1].size = (70, 135)
visel_body[2].size = (60, 80)
visel_body[3].size = (60, 120)
visel_body[4].size = (60, 100)
visel_body[5].size = (60, 110)

visel = AsyncImage(source='Images/viselitsa.png')
visel.size = (400, 400)

one_more_button_gfx = AsyncImage(source='Images/one_more.png')
one_more_button_gfx.size = (150, 50)
