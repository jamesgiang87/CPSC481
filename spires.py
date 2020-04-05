import pygame as rg
from setting import *
vec = rg.math.Vector2


class Player(rg.sprite.Sprite):
    def __init__(self, game):
        rg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = rg.Surface((30,40))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.pos = vec(width / 2, height / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        #jump on ground only
        self.rect.x += 1
        hits = rg.sprite.spritecollide(self, self.game.platforms,False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20
        hits = rg.sprite.spritecollide(self, self.game.ground,False)
        self.rect.x -= 1
        if hits:
            self.vel.y = -20

    def update(self):
        self.acc = vec(0, playerGrav)
        keys = rg.key.get_pressed()
        if keys[rg.K_LEFT]:
            self.acc.x = -playerAcc
        if keys[rg.K_RIGHT]:
            self.acc.x  = playerAcc

        #fraction
        self.acc.x += self.vel.x * playerFrict
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        #end of screen
        if self.pos.x > width:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = 0
        self.rect.midbottom = self.pos

    def attack(self):
        atk = rg.sprite.spritecollide(self, self.game.enemy,False)
        if keys[rg.K_A]:
            self.acc.x = -playerAcc

class Ground(rg.sprite.Sprite):
    def __init__ (self, x, y, w, h):
        rg.sprite.Sprite.__init__(self)
        self.image = rg.Surface((w,h))
        self.image.fill(lime)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Platform(rg.sprite.Sprite):
    def __init__ (self, x, y, w, h):
        rg.sprite.Sprite.__init__(self)
        self.image = rg.Surface((w,h))
        self.image.fill(white)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
