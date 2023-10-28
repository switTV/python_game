import pygame
import random
import sys

# Globals variables
HEIGHT = 600
WIDTH = 800
player_velocity = 0.5
enemyX_velocity = 0.6

# init
pygame.init()

# Create the screen
winScreen = pygame.display.set_mode((WIDTH, HEIGHT))

# title & logo
icon = pygame.image.load("./textures/ufo.png")

pygame.display.set_caption("Space invaders")
pygame.display.set_icon(icon)


# Player
class Player:
    def __init__(self):
        self.playerImg = pygame.image.load("./textures/player.png")
        self.playerX = 370
        self.playerY = 500

    def draw(self):
        winScreen.blit(self.playerImg, (self.playerX, self.playerY))

# Enemy

class Enemy:
    def __init__(self):
        self.enemyImg = pygame.image.load("./textures/enemy.png")
        self.enemyX = random.randint(0, 736)
        self.enemyY = 80
    
    def draw(self):
        winScreen.blit(self.enemyImg, (self.enemyX, self.enemyY))
    

# inicializando clases
player = Player()
enemy = Enemy()

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

    
    # Movemos el personaje en la dirección actual
    enemy.enemyX += enemyX_velocity
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #dibujar cosas en la pantalla
    player.draw()
    enemy.draw()

    # Uploading info
    pygame.display.update()