from pygame import *
from random import randint

#создай окно игры
window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('images.jpg'), (700,500))
# sprite1 = transform.scale(image.load('cyborg.png'), (100,100))
# sprite2 = transform.scale(image.load('hero.png'), (100,100))


score = 0


font.init()
font1 = font.SysFont('Arial', 70)
losee = font1.render('YOU LOSE!', True, (255, 215, 215))
win = font1.render('YOU WIN!', True, (255, 0, 255))
font = font.SysFont('Arial', 40)

finish = False

game = True
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 390:
            self.rect.y += self.speed

    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 390:
            self.rect.y += self.speed


class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > 500:
            self.rect.y = 0 
            self.rect.x = randint(100,650)
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y < 0:
            self.kill()

player = Player('raketka.png', 20, 390, 80, 100, 10)
player2 = Player('raketka2.png', 600, 390, 80, 100, 10)
ball = Enemy('ball.png', 350, 100, 25, 25, 5)


speed_x = 1
speed_y = 1


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player.update()
        player.reset()
        player2.update_l()
        player2.reset()
        ball.reset()
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        #отбитие мяча
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
        
        if ball.rect.y > 450:
            finish = True
            window.blit(losee, (200, 200))

    else:
        finish = False
        # score = 0
        # lost = 0
        # life = 3
        # for b in bullets:
        #     b.kill()
        # for m in monsters:
        #     m.kill()
        # for a in ast:
        #     a.kill()

        # time.delay(3000)

        



    display.update()
    clock.tick(FPS)