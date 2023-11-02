import pygame
import random

class Enemy:
    def __init__(self, winScreen, enemyX_velocity):
        
        self.winScreen = winScreen
        self.enemyImg = pygame.image.load("./textures/enemy.png")
        self.enemyX = random.randint(0, 736)
        self.enemyY = 80
        self.enemyX_velocity = enemyX_velocity

    def draw(self):
        self.winScreen.blit(self.enemyImg, (self.enemyX, self.enemyY))
