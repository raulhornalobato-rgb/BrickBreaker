import pygame
import random as rd

pygame.init()

Screen = pygame.display.set_mode((600,900))
pygame.display.set_caption("BrickBreaker")
Clock = pygame.time.Clock()
Game = True
WHITE = (255,255,255)
RED = (255,0,0)

PaddleX = 275
PaddleY = 800
BallX = rd.randint(50,550)
BallY = rd.randint(300,700)
WidthX = 1500
WidthY = 200

UpDown = True
RightLeft = True

while Game:
    Screen.fill((0,0,0))
    Clock.tick(180)
    Paddle = pygame.draw.rect(Screen,WHITE,(PaddleX,PaddleY,175,15))
    Ball = pygame.draw.circle(Screen,WHITE,(BallX,BallY),15)
    Barrier = pygame.draw.rect(Screen,RED,(0,100,WidthX,WidthY))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game = False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                PaddleX += 25
            elif event.key == pygame.K_a:
                PaddleX -= 25
    def BallMovementAndCollisions():
        global Paddle
        global Ball
        global Barrier

        global UpDown
        global RightLeft

        global BallX
        global BallY
        global WidthX
        global WidthY

        global Game

        #Movement
        if UpDown == True:
            BallY -= 1
        elif UpDown == False:
            BallY += 1
        if RightLeft == True:
            BallX += 1
        elif RightLeft == False:
            BallX -= 1

        #Bounce Part
        if BallX >= 580:
            RightLeft = False
        elif BallX <= 10:
            RightLeft = True
        if BallY >= 880:
            print("Game Over!")
            pygame.quit()
            Game = False
        elif BallY <= 10:
            print("You Win!")
            pygame.quit()
            Game = False

        #Paddle Collisions
        if Paddle.colliderect(Ball):
            UpDown = True
            Random = rd.randint(1,2)
            if Random == 1:
                RightLeft = True
            elif Random == 2:
                RightLeft = False
        #Barrier Collisions

        if Ball.colliderect(Barrier):
            WidthY -= 10
            UpDown = False
            Random = rd.randint(1,2)
            if Random == 1:
                RightLeft = True
            elif Random == 2:
                RightLeft = False
    BallMovementAndCollisions()
    pygame.display.update()
