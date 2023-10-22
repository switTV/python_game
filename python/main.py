import pygame
import sys

pygame.init()

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400

player_speed = 4

screenGame = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()



class Player:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 32, 32)
        
        self.x = int(x)
        self.y = int(y)
        
        self.velX = 0
        self.velY = 0
        
        self.color = ("aqua")

        self.left_pressed = False
        self.right_pressed = False

        self.speed = 4
    
    def draw(self, screenGame):
        pygame.draw.rect(screenGame, self.color, self.rect)
    
    def update(self):

        self.velX = 0
        self.velY = 0

        if self.left_pressed and not self.right_pressed:
            self.velX = -self.speed
            
        if self.right_pressed and not self.left_pressed:
            self.velX = self.speed

        self.x += self.velX
        self.y += self.velY

        self.rect = pygame.Rect(self.x, self.y, 32, 32)

player = Player(SCREEN_HEIGHT/2, SCREEN_WIDTH/2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.left_pressed = True
        player.right_pressed = False  # Asegúrate de desactivar la tecla opuesta
    elif keys[pygame.K_d]:
        player.right_pressed = True
        player.left_pressed = False  # Asegúrate de desactivar la tecla opuesta
    else:
        player.left_pressed = False
        player.right_pressed = False
        
    screenGame.fill((12, 24, 36))
    player.draw(screenGame)

    player.update()
    pygame.display.flip()
    clock.tick(60)