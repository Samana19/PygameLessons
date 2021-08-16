import pygame


#initializing pygame
pygame.init()
#Creating the screen
screen=pygame.display.set_mode((800,600))
#title and icon
pygame.display.set_caption("SPACE INVADERS")
icon=pygame.image.load('pycon.png')
pygame.display.set_icon(icon)

#adding player
playerimg=pygame.image.load("battleship.png")
playerX=370
playerY=480
playerX_change=0

def player(x,y):

    screen.blit(playerimg,(x,y))


#game loop
running=True

while running:
    screen.fill((255,208, 160))


    #playerY-=0.3

    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                # Increase to 0.3 if you want to increase the speed
                playerX_change=-0.1
            if event.key==pygame.K_RIGHT:
                playerX_change=0.1

        if event.type==pygame.KEYUP:

            if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
                playerX_change=0


    playerX+=playerX_change

    player(playerX,playerY)
    pygame.display.update()