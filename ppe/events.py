import pygame


class Events:
    def __init__(self):
        self.pressed_keys = []

    def get(self):
        self.pressed_keys = pygame.key.get_pressed()


events = Events()