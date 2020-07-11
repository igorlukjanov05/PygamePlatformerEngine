# test file
import pygame

import ppe


window = pygame.display.set_mode((1000, 1000))

while True:
    window.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()

    pygame.display.flip()
