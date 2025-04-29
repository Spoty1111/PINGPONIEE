from pygame import *
from PyQt5 import Qt

speed_x = 3
speed_y = 3
speed_x2 = 3
speed_y2 = 3
score = 0
score2 = 0


width, height = 700, 500
wall_WIDTH, wall_HEIGHT = 20, 200
ball_size = 65
ball_size2 = 40


score = 0
score2 = 0

#####################################################классы###########################################################################

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

class Player2(GameSprite):
    def update2(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 300:
            self.rect.y += self.speed

class Player(GameSprite):
    def update(self):
        keys_pressed = key.get_pressed()
        
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 300:
            self.rect.y += self.speed




background = transform.scale(image.load('newbackground.jpg'),(width,height))




################################обьекты классов,переменные(также на первых строчках)############################################################################

clock= time.Clock()
FPS = 60

ball = GameSprite('ball.png', width//2 - ball_size//2, height//2 - ball_size//2, ball_size, ball_size, 5)

ball2 = GameSprite('ball.png', width//3 - ball_size2//2, height//3 - ball_size2//2, ball_size2, ball_size2, 12)

wallie1 = Player('kitty.jpg', 0, height//2 - wall_WIDTH//2, wall_WIDTH, wall_HEIGHT, 10)

wallie2 = Player2('kitty.jpg', width-wall_WIDTH, height//2 - wall_WIDTH//2, wall_WIDTH, wall_HEIGHT, 10)


window = display.set_mode((width,height))

font.init()
font = font.SysFont('Arial',80)


display.set_caption('пингпонг')

game = True

finish = False
##################################################игровой цикл,отрисовка объектов###############################################################
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
    if finish != True:
        window.blit(background,(0,0))
        ball2.reset()
        ball.reset() 
        
        wallie1.update()
        wallie1.reset()
        wallie2.update2()
        wallie2.reset()

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        ball2.rect.x -= speed_x2
        ball2.rect.y -= speed_y2

        text = font.render(''+ str(score),1,(255,255,255))
        window.blit(text,(10,20))

        text2 = font.render(''+ str(score2),1,(255,255,255))
        window.blit(text2,(500,20))

############################################столкновения#############################################################################################
 
        if sprite.collide_rect(ball,wallie1):
            speed_x *= -1

        if sprite.collide_rect(ball,wallie2):
            speed_x *= -1

        if sprite.collide_rect(ball2,ball):
            speed_x *= -1
            speed_x2 *= -1
        if sprite.collide_rect(ball2,wallie1):
            speed_x2 *= -1

        if sprite.collide_rect(ball2,wallie2):
            speed_x2 *= -1
#################################################края############################################################################################
        if ball.rect.y <= 0 or ball.rect.y >= height - ball_size:
            speed_y *= -1
        
        if ball2.rect.y <= 0 or ball2.rect.y >= height - ball_size2:
            speed_y2 *= -1

########################################подсчет##############################################################################
        if ball.rect.x < 0:
            score += 1
            ball.rect.x = width//2 - ball_size//2
            ball.rect.y = height//2 - ball_size//2
            speed_x = 3
            speed_y = 3
        
        if ball.rect.x > width:
            score += 1
            ball.rect.x = width//2 - ball_size//2
            ball.rect.y = height//2 - ball_size//2
            speed_x = -3
            speed_y = 3
        
        
        if ball2.rect.x < 0 or ball2.rect.x > width:
            ball2.rect.x = width//2 - ball_size//2
            ball2.rect.y = height//2 - ball_size//2
            speed_x2 = -speed_x2
            speed_y2 = 3
            score2 += 1
    
        if score >= 10:
            text3 = font.render('левый выйграл!!',1,(255,255,0))
            window.blit(text3,(100,250))
            FPS = 1
        
            
        

        if score2 >=10: 
            text4 = font.render('правый выйграл!!',1,(255,255,0))
            window.blit(text4,(100,250))
            FPS = 1
        


            

        clock.tick(FPS)    
        display.update()

