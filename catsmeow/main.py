import pygame
from pygame import mixer
import random
import math

#initilizing the game
pygame.init()


#Creating the screen (W, H)
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
#background
background = pygame.image.load('background.png').convert()

#background sound
mixer.music.load('background_sound.wav')
mixer.music.play(-1)

#Title and ICON
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load('001-ufo.png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('animal.png')
playerX = 370
playerY = 480
playerX_change = 0

#enemy
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    enemyImg.append(pygame.image.load('cat.png'))
    enemyX.append(random.randint(0,735))
    enemyY.append(random.randint(50,150))
    enemyX_change.append(2)
    enemyY_change.append(40)

#bullet
bulletImg = pygame.image.load('bone.png')
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 15
#ready - you cant see the bullet on the screen
#fire - the bullet is moving
bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10

#Game Over text 
over_font = pygame.font.Font('freesansbold.ttf',64)

def show_score(x, y):
    score = font.render("score : " + str(score_value), True, (0,255,0))
    screen.blit(score, (x, y))

def game_over_text():
    over_text = over_font.render("GAME OVER", True, (255,255,255))
    screen.blit(over_text, (200, 250))

def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bulletImg, (x + 16, y + 10))

def isCollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX-bulletX, 2))+ (math.pow(enemyY-bulletY, 2)))
    if distance < 27:
        return True
    else:
        return False
def player(x, y):
    screen.blit(playerImg, (x, y))

def enemy(x, y, i):
    screen.blit(enemyImg[i], (x, y))

#Game loop - Makes sure the game is running.
running = True
while running:

    #Add color to the screen, Replaceable with a photo?
    screen.fill((0, 0, 0))

    #Background image
    screen.blit(background,(0, 0))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
        # if keystroke is pressed check wherther is right or left
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -3
            if event.key == pygame.K_RIGHT:
                playerX_change = 3
            if event.key == pygame.K_SPACE:
                if bullet_state is "ready":
                    bullet_sound = mixer.Sound('woof.wav')
                    bullet_sound.play()
                    bulletX = playerX
                    fire_bullet(bulletX, bulletY)


        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    #Keeps player in the screen
    playerX += playerX_change

    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    #Keeps enemy in the screen and helps to move it
    for i in range(num_of_enemies):
        #Game OVer
        if enemyY[i] > 440:
            for j in range(num_of_enemies):
                enemyY[j] = 2000
            game_over_text()
            break


        enemyX[i] += enemyX_change[i]
        if enemyX[i] <=0:
            enemyX_change[i] = 3
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >=736:
            enemyX_change[i] = -3
            enemyY[i] += enemyY_change[i]
        
        collision = isCollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            explosion_sound = mixer.Sound('cat_screem.wav')
            explosion_sound.play()
            bulletY = 480
            bullet_state = "ready"
            score_value += 1
            enemyX[i] = random.randint(0,735)
            enemyY[i] = random.randint(50,150)
        enemy(enemyX[i], enemyY[i], i)

    #Bullet movement
    if bulletY <=0:
        bulletY= 480
        bullet_state="ready"

    if bullet_state is "fire":
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletY_change
        
    player(playerX, playerY)
    show_score(textX, textY)
    pygame.display.update()
    print(clock.tick(60))