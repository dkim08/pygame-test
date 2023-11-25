import pygame as pg
from os import listdir

pg.init()
pg.font.init()

music = None
music_list = list()
indx = 0
music_list = listdir('files')
volume = 0.5

# Создаем окно
win = pg.display.set_mode((300, 200))
pg.display.set_caption("Music Box")
# Загружаем бэкграунд
bg = pg.transform.scale(pg.image.load('img/bg.jpg'), (300, 200))
# Настраиваем шрифт
font_config = pg.font.Font(None, 24)

# Выбираем следующий файл из папки
def next_song():
    global music_list, indx
    indx += 1
    if indx >= len(music_list):
        indx = 0
    return pg.mixer.Sound('files/'+music_list[indx])
    

while True:
    # Проверка нажатия на крестик
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()

    # Пишем название песни на фоне
    song_name = font_config.render(music_list[indx], True, (255, 215, 0))
    # Обновляем фон
    win.blit(bg, (0, 0))

    # Получаем все нажатые клавиши
    keys = pg.key.get_pressed()

    # Проверяем какая нажата
    if keys[pg.K_SPACE]:
        if music is not None:
            music.stop()
        # Переключаем песню
        music = next_song()
        music.play()

    # Увеличиваем громкость
    elif keys[pg.K_UP] and volume < 1:
        volume += 0.1

    # Уменьшаем громкость
    elif keys[pg.K_DOWN] and volume > 0:
        volume -= 0.1
        
    if music is not None:
        music.set_volume(volume)
        # Обновляем название песни
        win.blit(song_name, (5, 5))
    
    pg.display.update()
    pg.time.delay(40)
