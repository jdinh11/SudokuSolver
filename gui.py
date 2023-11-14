import pygame 

DIMENSION = 800

pygame.init()
screen = pygame.display.set_mode((DIMENSION, DIMENSION))
running = True

while running: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")

pygame.quit()