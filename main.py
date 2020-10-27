import pygame
import math
import random

# initiaalise pygame
pygame.init()

# create the screen
screen = pygame.display.set_mode((800, 600))

# background
spacebg1 = pygame.image.load("spacebg1.png")

# CAption and icon
pygame.display.set_caption("SHAREEF's GAME")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# player
PlayerImg = pygame.image.load("sp orig.png")
Playerx = 370
Playery = 480
Playerx_change = 0

# enemy
EnemyImg = []
Enemyx = []
Enemyy = []
Enemyx_change = []
Enemyy_change = []
num_of_enemies = 6

for i in range(num_of_enemies):
    EnemyImg.append(pygame.image.load("enemy1.png"))
    Enemyx.append(random.randint(0, 735))
    Enemyy.append(random.randint(50, 150))
    Enemyx_change.append(2)
    Enemyy_change.append(40)

# bullet
BulletImg = pygame.image.load("bullet.png")
Bulletx = 0
Bullety = 480
Bulletx_change = 0
Bullety_change = 5
# ready = cant see bullet on screen
# fire = bullet is curently moving
Bullet_state = "ready"

#score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)

textx = 10
texty = 10

def show_score(x, y):
    score = font.render("score :" + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))

def Player(x, y):
    screen.blit(PlayerImg, (x, y))  # (drawing=blit) image


def Enemy(x, y, i):
    screen.blit(EnemyImg[i], (x, y))


def fire_bullet(x, y):
    global Bullet_state
    Bullet_state = "fire"
    screen.blit(BulletImg, (x + 16, y + 10))


def iscollision(Enemyx, Enemyy, Bulletx, Bullety):
    distance = math.sqrt((math.pow(Enemyx - Bulletx, 2)) + (math.pow(Enemyy - Bullety, 2)))
    if distance < 27:
        return True
    else:
        return False


# game loop
running = True
while running:

    screen.fill((0, 255, 255))  # rgb colours

    # background image
    screen.blit(spacebg1, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # if keystroke is pressed check whether its right or not
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                Playerx_change = -4
            if event.key == pygame.K_RIGHT:
                Playerx_change = 4
            if event.key == pygame.K_SPACE:
                if Bullet_state is "ready":
                    Bulletx = Playerx
                    fire_bullet(Bulletx, Bullety)
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                Playerx_change = 0

    # checking for boundaries
    Playerx += Playerx_change

    if Playerx <= 0:
        Playerx <= 0
    elif Playerx >= 736:
        Playerx = 736

    # enemy movement
    for i in range(num_of_enemies):
        Enemyx[i] += Enemyx_change[i]

        if Enemyx[i] <= 0:
            Enemyx_change[i] = 2
            Enemyy[i] += Enemyy_change[i]
        elif Enemyx[i] >= 736:
            Enemyx_change[i] = -2
            Enemyy[i] += Enemyy_change[i]
        # collision
        collision = iscollision(Enemyx[i], Enemyy[i], Bulletx, Bullety)
        if collision:
            Bullety = 480
            Bullet_state = 'ready'
            score_value += 1

            Enemyx[i] = random.randint(0, 735)
            Enemyy[i] = random.randint(50, 150)

        Enemy(Enemyx[i], Enemyy[i], i)

    # bullet movement
    if Bullety <= 0:
        Bullety = 480
        Bullet_state = "ready"

    if Bullet_state is "fire":
        fire_bullet(Bulletx, Bullety)
        Bullety -= Bullety_change



    Player(Playerx, Playery)
    show_score(textx, texty)

    pygame.display.update()  # screen to refresh and colors and events to be applied
