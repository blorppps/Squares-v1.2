#launcher
'START BLOCK'
from tkinter import *
launcher = Tk()
launcher.geometry('100x100')

def start():
    launcher.destroy()

hard = IntVar()
title = Label(launcher,text='Squares')
button = Button(launcher,text='Launch',bd='2',command=start)
checkbox = Checkbutton(launcher,text='Hard Mode',variable=hard)

title.pack()
checkbox.pack()
button.pack()
mainloop()
'END BLOCK'

#setup
'START BLOCK'
import keyboard
import pygame
import random
import math
import time

running = True
score = 0
FPS = 300
fpsclock = pygame.time.Clock()

pygame.init()

window = pygame.display.set_mode((800,600))
if hard.get() == 1:
    pygame.display.set_caption('Squares v1.2 - Hard Mode')
else:
    pygame.display.set_caption('Squares v1.2')
icon = pygame.image.load('assets\enemy.png')
pygame.display.set_icon(icon)
'END BLOCK'

#score
'START BLOCK'
font = pygame.font.Font('freesansbold.ttf',32)
def show_score():
    global score
    if hard.get() == 1:
        score_display = font.render(str(score),True,(255,0,0))
        window.blit(score_display,(10,10))
    else:
        score_display = font.render(str(score),True,(255,255,255))
        window.blit(score_display,(10,10))
'END BLOCK'

#player
'START BLOCK'
playerX = 768
playerY = 0
left = False
right = False
up = False
down = False
playersprite = pygame.image.load('assets\player.png')
def player(x,y):
    window.blit(playersprite,(x,y))
'END BLOCK'

#enemy 1
'START BLOCK'
enemy1X = 384
enemy1Y = 75
enemy1state = 1
enemy1sprite = pygame.image.load('assets\enemy.png')
def enemy1(x,y):
    window.blit(enemy1sprite,(x,y))
def enemy1check():
    global running
    if enemy1X + 32 > playerX and enemy1X < playerX + 32 and enemy1Y < playerY + 32 and enemy1Y + 32 > playerY:
        running = False
'END BLOCK'

#enemy 2
'START BLOCK'
enemy2X = 400
enemy2Y = 300
enemy2Xmove = random.uniform(-0.5,0.5)
enemy2Ymove = random.uniform(-0.5,0.5)
enemy2sprite = pygame.image.load('assets\enemy.png')
def enemy2(x,y):
    window.blit(enemy2sprite,(x,y))
def enemy2check():
    global running
    if enemy2X + 32 > playerX and enemy2X < playerX + 32 and enemy2Y < playerY + 32 and enemy2Y + 32 > playerY:
        running = False
def bounce():
    global enemy2Xmove
    global enemy2Ymove
    enemy2Xmove = random.uniform(-0.5,0.5)
    enemy2Ymove = random.uniform(-0.5,0.5)
'END BLOCK'

#enemy 3
'START BLOCK'
enemy3X = 400
enemy3Y = 500
enemy3Xmove = 0
enemy3Ymove = 0
enemy3sprite = pygame.image.load('assets\enemy.png')
def enemy3(x,y):
    window.blit(enemy3sprite,(x,y))
def enemy3check():
    global running
    if enemy3X + 32 > playerX and enemy3X < playerX + 32 and enemy3Y < playerY + 32 and enemy3Y + 32 > playerY:
        running = False
'END BLOCK'

#coin
'START BLOCK'
coinX = random.randint(0,784)
coinY = random.randint(0,584)
coinsprite = pygame.image.load('assets\coin.png')
def coin(x,y):
    window.blit(coinsprite,(x,y))
def coincheck():
    global score
    global coinX
    global coinY
    if coinX + 32 > playerX and coinX < playerX + 32 and coinY < playerY + 32 and coinY + 32 > playerY:
        score = score + 1
        coinX = random.randint(0,784)
        coinY = random.randint(0,584)
'END BLOCK'

#main loop
while running:
    
    window.fill((0,0,0))

    #closes window when x is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #movement
    'START BLOCK'
    if keyboard.is_pressed('d') or keyboard.is_pressed('right'):
        playerX = playerX + 0.6
    if keyboard.is_pressed('a') or keyboard.is_pressed('left'):
        playerX = playerX - 0.6
    if keyboard.is_pressed('w') or keyboard.is_pressed('up'):
        playerY = playerY - 0.6
    if keyboard.is_pressed('s') or keyboard.is_pressed('down'):
        playerY = playerY + 0.6
    #makes it so the player cant leave the window
    if playerX < 0:
        playerX = 0
    if playerX > 768:
        playerX = 768
    if playerY < 0:
        playerY = 0
    if playerY > 568:
        playerY = 568

    player(playerX,playerY)
    'END BLOCK'

    #enemy 1
    'START BLOCK'
    if enemy1state == 1:
        enemy1X = enemy1X - 0.2
        enemy1Y = enemy1Y + 0.3
        if enemy1Y > 500:
            enemy1state = 2
    elif enemy1state == 2:
        enemy1X = enemy1X + 0.3
        if enemy1X > 670:
            enemy1state = 3
    elif enemy1state == 3:
        enemy1X = enemy1X - 0.2
        enemy1Y = enemy1Y - 0.3
        if enemy1Y < 75:
            enemy1state = 1
            enemy1X = 384
            enemy1Y = 75
    
    enemy1check()
    
    enemy1(enemy1X,enemy1Y)
    'END BLOCK'

    #enemy 2
    'START BLOCK'
    enemy2X = enemy2X + enemy2Xmove
    enemy2Y = enemy2Y + enemy2Ymove

    if enemy2X < 0:
        enemy2X = 0
        bounce()
    if enemy2X > 768:
        enemy2X = 768
        bounce()
    if enemy2Y < 0:
        enemy2Y = 0
        bounce()
    if enemy2Y > 568:
        enemy2Y = 568
        bounce()

    enemy2check()

    enemy2(enemy2X,enemy2Y)
    'END BLOCK'

    #enemy 3
    'START BLOCK'
    if playerX > enemy3X:
        enemy3Xmove = 0.2
    if playerX < enemy3X:
        enemy3Xmove = -0.2
    if playerY > enemy3Y:
        enemy3Ymove = 0.2
    if playerY < enemy3Y:
        enemy3Ymove = -0.2

    if hard.get() == 1:
        enemy3Xmove = enemy3Xmove * 1.5
        enemy3Ymove = enemy3Ymove * 1.5
    
    enemy3X = enemy3X + enemy3Xmove
    enemy3Y = enemy3Y + enemy3Ymove

    enemy3check()
    
    enemy3(enemy3X,enemy3Y)
    'END BLOCK'

    #coin
    'START BLOCK'
    coincheck()
    coin(coinX,coinY)
    'END BLOCK'

    show_score()
    pygame.display.update()
    fpsclock.tick(FPS)

#ending
'START BLOCK'
pygame.quit()

endscreen = Tk()
endscreen.geometry('100x100')
gameover = Label(text='Game Over')
finalscore = Label(text='Score: ' + str(score))
quitbutton = Button(text='Quit',command=endscreen.destroy)
harddisplay = Label(text='Hard Mode',fg='#ff0000')

if hard.get() == 1:
    harddisplay.pack()
gameover.pack()
finalscore.pack()
quitbutton.pack()
mainloop()
'END BLOCK'
