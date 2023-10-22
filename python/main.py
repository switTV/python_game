import pygame
import sys

# Globals variables
HEIGHT = 600
WIDTH = 800

# init
pygame.init()

# Create the screen
winScreen = pygame.display.set_mode((WIDTH, HEIGHT))

# title & logo
icon = pygame.image.load("./textures/ufo.png")

pygame.display.set_caption("Space invaders")
pygame.display.set_icon(icon)

# Principal loop
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Changing BG color
    winScreen.fill((22, 29, 54))

    # Uploading info
    pygame.display.update()