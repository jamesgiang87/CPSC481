import pygame as rg
from vector import Vector as vec
from pygame.sprite import Sprite
from setting import *


class Player(Sprite):
    def __init__(self, game):
        super().__init__()
        self.game = game
        self.image = rg.Surface((30,60))
        self.image.fill(yellow)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.test = Test(self.rect)


    def update(self):
        self.acc = vec(0, 0)
        keys = rg.key.get_pressed()
        if keys[rg.K_LEFT]:
            self.acc.x = -playerAcc
        if keys[rg.K_RIGHT]:
            self.acc.x = playerAcc
        if keys[rg.K_SPACE]:
            self.test.setrec(self.rect)
            self.test.move((0,1))
            if 0 != len(rg.sprite.spritecollide(self.test, self.game.walls, False)):
                self.acc.y = -playerJump
        if keys[rg.K_DELETE]:
            self.game.playing = False
        if keys[rg.K_ESCAPE]:
            self.game.playing = False
            self.game.running = False

        # fraction
        self.acc.x += self.vel.x * playerFrict
        self.acc.y += playerGravity
        self.vel += self.acc
        # move up/down and collide with walls
        self.rect.y += self.vel.y + 0.5 * self.acc.y
        hit = rg.sprite.spritecollide(self, self.game.walls, False)
        if 0 != len(hit):
            if 0 > self.vel.y:
                self.rect.top = hit[0].rect.bottom
            else:
                self.rect.bottom = hit[0].rect.top
            self.acc.y = 0
            self.vel.y = 0
        # move left/right and collide with walls
        self.rect.x += self.vel.x + 0.5 * self.acc.x
        hit = rg.sprite.spritecollide(self, self.game.walls, False)
        if 0 != len(hit):
            if 0 > self.vel.x:
                self.rect.left = hit[0].rect.right
            else:
                self.rect.right = hit[0].rect.left
            self.acc.x = 0
            self.vel.x = 0


class Test(Sprite):
    def __init__(self, rect):
        super().__init__()
        self.rect = rg.Rect(rect.x, rect.y, rect.width, rect.height)

    def setrec(self, rect):
        self.rect = rg.Rect(rect.x, rect.y, rect.width, rect.height)

    def move(self, vel):
        self.rect.x += vel[0]
        self.rect.y += vel[1]
