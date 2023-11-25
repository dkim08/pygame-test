import pygame as pg

pg.init()
window = pg.display.set_mode((300,300))
pg.display.set_caption("Это заголовок окна")

# заливка экрана
window.fill((255,213,91))


# # Игровой цикл
while True:

    # Проверка нажатия на крестик окна
    for ev in pg.event.get():
        print(ev)
        if ev.type == pg.QUIT:
            pg.quit()
    
    # Обновляем экран
    pg.display.update()
    # задержка обновления
    pg.time.delay(40)
