import pygame as pg
from os import listdir
from random import choice
# dvelop branch
pg.init()
pg.font.init()

screen = pg.display.set_mode((500, 300))
pg.display.set_caption("Music Box")
clock = pg.time.Clock()
running = True
clr = (255, 255, 255, 255)
clr2 = (0, 225, 0)
clr3 = (255, 0, 225)
color = ['red', 'orange', 'yellow', 'green', 'blue']

music = None
music_list = listdir('files')
# print(type(music_list))
index = 0
volume = 0.5

image = pg.image.load('img/bg.jpg')
bg = pg.transform.scale(image, (500, 300))
font_config = pg.font.Font(None, 24)

def next_song():
    global music_list, index
    index += 1
    if index >= len(music_list):
        index = 0
    return pg.mixer.Sound('files/'+ music_list[index])

# music = next_song()
# music.play()
song_name = font_config.render(music_list[index], True, (255, 215, 0))
screen.blit(bg, (0, 0))
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # keys = pg.key.get_pressed()
        # if keys[pg.K_1] == True:
        #     screen.fill(clr)
        # elif keys[pg.K_2] == True:
        #     screen.fill(clr2)
        # elif keys[pg.K_3] == True:
        #     screen.fill(clr3) 

        keys = pg.key.get_pressed()


    if keys[pg.K_SPACE]:
        if music is not None:
            music.stop()

        music = next_song()
        music.play()

    elif keys[pg.K_UP] and volume < 1:
        volume += 0.1

    elif keys[pg.K_DOWN] and volume > 0:
        volume -= 0.1
        
    if music is not None:
        music.set_volume(volume)

        
    screen.fill('purple') 
    screen.blit(song_name, (105, 105))
    random_clr = choice(color)
    pg.display.update()
    clock.tick(60)