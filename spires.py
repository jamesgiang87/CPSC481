import pygame as rg
from setting import *
vec = rg.math.Vector2


class Player(rg.sprite.Sprite):
    def __init__(self):
        rg.sprite.Sprite.__init__(self)
        self.image = rg.Surface((30,40))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.pos = vec(width / 2, height / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)


    def update(self):
        self.acc = vec(0, 0)
        keys = rg.key.get_pressed()
        if keys[rg.K_LEFT]:
            self.acc.x = -playerAcc
        if keys[rg.K_RIGHT]:
            self.acc.x  = playerAcc

        #fraction
        self.acc += self.vel * playerFrict
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #wrap screen
        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = width
        self.rect.center = self.pos
