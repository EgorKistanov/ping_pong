from pygame import *


WINDOW_SIZE = (700, 500)
SPRITE_SIZE = (50, 50)

FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, sprite_size=SPRITE_SIZE):
        super().__init__()
        self.image = transform.scale(image.load(player_image), sprite_size)
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < WINDOW_SIZE[1] - 105:
            self.rect.y += self.speed
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < WINDOW_SIZE[1] - 105:
            self.rect.y += self.speed

window = display.set_mode(WINDOW_SIZE)
display.set_caption('Ping-pong')
window.fill((0, 0, 255))

rocket_1 = Player("image/Прямоугольник.png", 50, 250, 5, (25, 100))
rocket_2 = Player("image/Прямоугольник.png", 625, 250, 5, (25, 100))
ball = GameSprite("image/мяч.png", 300, 200, 5)
clock = time.Clock()

game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill((0, 0, 255))
        rocket_1.update_l()
        rocket_2.update_r()
        rocket_1.reset()
        rocket_2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)