import pygame

class Player:
    def __init__(self, winScreen, player_velocity):
        self.winScreen = winScreen
        self.playerImg = pygame.image.load("./textures/player.png")
        self.playerX = 370
        self.playerY = 500
        self.player_velocity = player_velocity

    def draw(self):
        self.winScreen.blit(self.playerImg, (self.playerX, self.playerY))
