from pygame import *
from random import randint

#создай окно игры
window = display.set_mode((700,500))
display.set_caption('Пинг-Понг')
background = transform.scale(image.load('images.jpg'), (700,500))


score = 0
score2 = 0

font.init()
font1 = font.SysFont('Arial', 30)
losee = font1.render('PLAYER 1 LOSE', True, (255, 215, 215))
losee2 = font1.render('PLAYER 2 LOSE', True, (255, 0, 255))
win1 = font1.render('PLAYER 1 WIN', True,(255,0,255))
win2 = font1.render('PLAYER 2 WIN', True,(255,0,255))

game = True
finish = False
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
    def update_k(self):
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

player = Player('raketka.png', 20, 390, 80, 100, 10)
player2 = Player('raketka2.png', 600, 390, 80, 100, 10)
ball = Player('ball.png', 350, 100, 25, 25, 5)


speed_x = randint(1,3)
speed_y = randint(1,3)


while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.blit(background, (0,0))
        player.update_k()
        
        player2.update_l()
        
        ball.rect.x += speed_x
        ball.rect.y += speed_y

        text = font1.render('Счет 1 игрока:' + str(score), 1, (255, 255, 255))
        window.blit(text, (10, 20))

        text2 = font1.render('Счет 2 игрока:' + str(score2), 1, (255, 255, 255))
        window.blit(text2, (10, 60))

        #отбитие мяча
        if ball.rect.y > 450 or ball.rect.y < 0:
            speed_y *= -1
        if sprite.collide_rect(player, ball) or sprite.collide_rect(player2, ball):
            speed_x *= -1
            speed_y *= 1

        if ball.rect.y > 500:
            ball.rect.x = 0 
            ball.rect.x = randint(100,650)
        
        if ball.rect.x < 0:
            finish = True
            window.blit(losee, (200, 200))
            game = True

        if ball.rect.x > 700:
            finish = True
            window.blit(losee2, (200, 200))
            game = True

        if sprite.collide_rect(player, ball):
            randint(1,5)
            randint(1,5)

        if sprite.collide_rect(player2, ball):
            randint(1,5)
            randint(1,5)

        if sprite.collide_rect(player, ball):
            score += 1

        if sprite.collide_rect(player2, ball):
            score2 += 1

        if score >= 5:
            finish = True
            window.blit(win1, (200, 200))

        if score2 >= 5:
            finish = True
            window.blit(win2, (200, 200))

        player.reset()
        player2.reset()
        ball.reset()
    # else:
    #     finish = False
    #     score = 0

    display.update()
    clock.tick(FPS)
