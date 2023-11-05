import pygame
import numpy

class Bullet:
    def __init__(self, winScreen):
        self.winScreen = winScreen
        self.bulletImg = pygame.image.load("./textures/bullet.png")
        self.bullet_state = False # if is false you can't see it, but if is true you can see the bullet
        self.bulletY = 500
        self.bulletX = 0

    def fire_bullet(self,x, y):
        self.bullet_state = True
        self.winScreen.blit(self.bulletImg, (x+16, y+10))

    def isCollition(params ,enemyX, enemyY, bulletX, bulletY):
        distance = numpy.sqrt((numpy.power(enemyX-bulletX, 2)) + (numpy.power(enemyY-bulletY, 2)))

        if distance < 27:
            return True
        else:
            return False

    def draw(self):
        self.winScreen.blit(self.bulletImg, (self.bulletX, self.bulletY))
