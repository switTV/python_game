import pygame
from player import Player
from enemy import Enemy
from bullet import Bullet
from config import *

# init
pygame.init()

# Create the screen
winScreen = pygame.display.set_mode((WIDTH, HEIGHT))

# title & logo
icon = pygame.image.load("./textures/ufo.png")

pygame.display.set_caption("Space invaders")
pygame.display.set_icon(icon)


# inicializando clases
player = Player(winScreen, player_velocity)
enemy = Enemy(winScreen, enemyX_velocity)
bullet = Bullet(winScreen)

# Principal loop
running = True
while running:

    # Changing BG color
    winScreen.fill((22, 29, 54))
    
    #Player movement
    key = pygame.key.get_pressed()
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        player.playerX -= player_velocity

    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        player.playerX += player_velocity
    
    if key[pygame.K_SPACE]:
        if bullet.bullet_state == True:
            pass
        else:
            bullet.bulletX = player.playerX
        bullet.bullet_state = True
    


    #adding boundaries to my game
    if player.playerX <= 0:
        player.playerX = 0

    elif player.playerX >= 736:
        player.playerX = 736

    
    # Enemy movement
    if enemy.enemyX <= 0:
        enemyX_velocity = abs(enemyX_velocity)
        enemy.enemyY += 10

    if enemy.enemyX >= 736:
        enemyX_velocity = -abs(enemyX_velocity)
        enemy.enemyY += 10

    # Bullet Movement
    if bullet.bullet_state is True:
        bullet.fire_bullet(bullet.bulletX, bullet.bulletY)
        bullet.bulletY -= bullet_velocity

        if bullet.bulletY <= -70:
            bullet.bullet_state = False
            bullet.bulletY = 500

    
    # Movemos el enemigo en la dirección actual
    enemy.enemyX += enemyX_velocity
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #dibujar cosas en la pantalla
    player.draw()
    enemy.draw()

    # Uploading info
    pygame.display.update()