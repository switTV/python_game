import pygame
import sys

# Globals variables
HEIGHT = 600
WIDTH = 800

# init
pygame.init()

# Create the screen
winScreen = pygame.display.set_mode((WIDTH, HEIGHT))

# title

# Principal loop
running= True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False