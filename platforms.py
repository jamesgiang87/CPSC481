import pygame as rg
from pygame.sprite import Sprite
from setting import *
from vector import Vector as vec


class Wall(Sprite):
    def __init__(self, game, x, y, w, h):
        super().__init__()
        self.game = game
        self.image = rg.Surface((w, h))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.pos = vec(x, y)

    def update(self):
        pass

