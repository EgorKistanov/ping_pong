from pygame import *


WINDOW_SIZE = (700, 500)
SPRITE_SIZE = (50, 50)

FPS = 60



window = display.set_mode(WINDOW_SIZE)
display.set_caption('Ping-pong')
window.fill((0, 0, 255))

clock = time.Clock()

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)