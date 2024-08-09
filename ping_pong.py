from pygame import *
from random import randint

WINDOW_SIZE = (700, 500)
SPRITE_SIZE = (50, 50)
speed_x = 3
speed_y = 3
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


def random_speed(speed_x, speed_y):
    number = randint(0, 1)
    if number == 0:
        speed_x *= -1
    else:
        speed_x *= 1
    number = randint(0, 1)
    if number == 1:
        speed_y *= -1
    else:
        speed_y *= 1
    return speed_x, speed_y




window = display.set_mode(WINDOW_SIZE)
display.set_caption('Ping-pong')
window.fill((0, 0, 255))

rocket_1 = Player("image/Прямоугольник.png", 50, 250, 5, (25, 100))
rocket_2 = Player("image/Прямоугольник.png", 625, 250, 5, (25, 100))
ball = GameSprite("image/мяч.png", 300, 200, 5)
clock = time.Clock()

font.init()
font1 = font.Font(None, 36)


speed_x, speed_y = random_speed(speed_x, speed_y)

game = True
finish = False
score_left = 0
score_right = 0
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if not finish:
        window.fill((0, 0, 255))
        rocket_1.update_l()
        rocket_2.update_r()

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if ball.rect.y < 0 or ball.rect.y > WINDOW_SIZE[1] - 50:
            speed_y *= -1
        if sprite.collide_rect(rocket_1, ball) or sprite.collide_rect(rocket_2, ball):
            speed_x *= -1

        if ball.rect.x < 0:
            score_left += 1
            ball.rect.x = 300
            ball.rect.y = 200
            ball.reset()
            speed_x, speed_y = random_speed(speed_x, speed_y)
        if ball.rect.x > WINDOW_SIZE[0]:
            score_right += 1
            ball.rect.x = 300
            ball.rect.y = 200
            ball.reset()
            speed_x, speed_y = random_speed(speed_x, speed_y)

        text_left = font1.render('Пропущено: ' + str(score_left), 1, (255, 255, 255))
        text_right = font1.render('Пропущено: ' + str(score_right), 1, (255, 255, 255))
        window.blit(text_left, (20, 20))
        window.blit(text_right, (500, 20))

        rocket_1.reset()
        rocket_2.reset()
        ball.reset()

    display.update()
    clock.tick(FPS)