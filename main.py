#setup
'START BLOCK'
import pygame
import keyboard
import random

running = True
score = 0
FramesSinceEnemy = 0
gamespeed = 0

pygame.init()
window = pygame.display.set_mode((800,600))
pygame.display.set_icon(pygame.image.load('assets\enemyright.png'))
pygame.display.set_caption('Anti-Semitism Simulator - Python Remake')

font = pygame.font.Font('freesansbold.ttf',32)
def show_score():
    score_display = font.render(str(score),True,(255,255,255))
    window.blit(score_display,(10,10))

FPS = 300
fpsclock = pygame.time.Clock()
'END BLOCK'

#player
'START BLOCK'
playersprite = pygame.image.load('assets\player.png')

playerX = 384
playerY = 384

def player(x,y):
    window.blit(playersprite,(x,y))

poking = False
stickstate = 0
stickcooldown = 0
pokedirection = 0
'END BLOCK'

#enemies
'START BLOCK'
enemyspriteleft = pygame.image.load('assets\enemyleft.png')
enemyspriteright = pygame.image.load('assets\enemyright.png')

enemyXs = []

def createenemy():
    global enemyXs
    if random.randint(0,1) == 1:
        enemyXs.append(0)
    else:
        enemyXs.append(768)

def enemies():
    global enemyXs
    global score
    global running
    for i in range (len(enemyXs)):
        
        enemyX = enemyXs[i]

        #chase player
        if enemyX > playerX:
            enemyXs.pop(i)
            enemyXs.insert(i,enemyX-0.2)
            window.blit(enemyspriteleft,(enemyX,384))
        if enemyX < playerX:
            enemyXs.pop(i)
            enemyXs.insert(i,enemyX+0.2)
            window.blit(enemyspriteright,(enemyX,384))

        #die if poked
        if stickstate == 1 and pokedirection == 0:
            if enemyX < playerX-stick and enemyX + 32 > playerX-35-stick:
                enemyXs.pop(i)
                score = score + 1
                break
        if stickstate == 1 and pokedirection == 1:
            if enemyX + 32 > playerX+32+stick and enemyX < playerX+67+stick:
                enemyXs.pop(i)
                score = score + 1
                break

        #kill if touching player
        if enemyX + 32 > playerX and enemyX < playerX + 32 and 384 < playerY + 32 and 416 > playerY:
            running = False
'END BLOCK'

#main loop
while running:

    window.fill((0,0,0))
    pygame.draw.line(window,(255,255,255),(0,416),(800,416),1)
    
    #quit
    'START BLOCK'
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    'END BLOCK'

    #player
    'START BLOCK'
    if keyboard.is_pressed('d') or keyboard.is_pressed('right'):
        playerX = playerX + 1
    if keyboard.is_pressed('a') or keyboard.is_pressed('left'):
        playerX = playerX - 1

    if playerX < 0:
        playerX = 0
    if playerX > 768:
        playerX = 768

    #stick
    #for stickstate, 0 = inactive, 1 = poking, 2 = retracting
    #for pokedirection, 0 = left, 1 = right

    #starts poke
    if stickstate == 0 and stickcooldown == 0:
        if keyboard.is_pressed('q'):
            stickstate = 1
            stick = 0
            pokedirection = 0
        elif keyboard.is_pressed('e'):
            stickstate = 1
            stick = 0
            pokedirection = 1

    #moves stick
    if not stickstate == 0:
        if pokedirection == 0:
            pygame.draw.line(window,(160,82,45),(playerX-stick,400),(playerX-35-stick,400),2)
        elif pokedirection == 1:
            pygame.draw.line(window,(160,82,45),(playerX+32+stick,400),(playerX+67+stick,400),2)
        if stickstate == 1:
            stick = stick + 0.7
            if stick > 20:
                stickstate = 2
        if stickstate == 2:
            stick = stick - 0.7
            if stick < 0:
                stickstate = 0
                stickcooldown = 200
    else:
        if stickcooldown > 0:
            stickcooldown = stickcooldown - 1

    player(playerX,playerY)
    'END BLOCK'

    #enemies
    'START BLOCK'
    FramesSinceEnemy = FramesSinceEnemy + 1
    if FramesSinceEnemy > 1000:
        createenemy()
        FramesSinceEnemy = random.randint(-400,0) + gamespeed
    enemies()
    'END BLOCK'

    fpsclock.tick(FPS)
    if gamespeed < 800:
        gamespeed = gamespeed + 0.02
    show_score()
    pygame.display.update()
    
#ending
'START BLOCK'
pygame.quit()
'END BLOCK'
