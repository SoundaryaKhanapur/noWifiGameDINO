import pygame

pygame.init()

#game window
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("DINO NO WIFI GAME")

#game loop so that game window remains till user closes it
gameRunnning = True
while gameRunnning:
    #fill screen with color
    screen.fill((255, 255, 255))

    #event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunnning = False #exit out of game loop

    #update the game
    pygame.display.update()