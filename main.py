# test file
import pygame
import ppe


window = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()

game_object = ppe.game_object.GameObject(pygame.Surface((100, 100)), (100, 100))

while True:
    game_object.x += 1
    window.fill((255, 255, 255))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            exit()
    game_object.blit(window)
    clock.tick(50)
    pygame.display.flip()
