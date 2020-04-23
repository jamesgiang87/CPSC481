import pygame as rg
from setting import *
from random import choice, randrange
vec = rg.math.Vector2



playerResizeX = 75
playerResizeY = 30

class SpriteSheet:
    def __init__(self, filename):
        self.spritesheet = rg.image.load(filename).convert()

    def getImage(self, x, y, width, height):
        image = rg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = rg.transform.scale(image, (width // 5, height // 5))
        return image


class Player(rg.sprite.Sprite):
    def __init__(self, game):
        rg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = False
        self.jumping = False
        self.attacking = False
        self.currentFrame = 0
        self.lastUpdate = 0
        self.loadImages()
        self.image = self.idleFrameR[0]
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
        self.pos = vec(width / 2, height / 2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)
        self.facing = 1
        self.attacking = False
        self.rcopy = self.rect.copy()
        self.star = False

    def loadImages(self):

        self.walkingFrameR = [
        self.game.spritesheet.getImage(1179 - playerResizeX, 3634 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(1768 - playerResizeX, 3634 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(2357 - playerResizeX, 3634 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(2946 - playerResizeX, 3634 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(3535 - playerResizeX, 3634 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(4124 - playerResizeX, 3634 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(4713 - playerResizeX, 3634 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(5302 - playerResizeX, 3634 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(5891 - playerResizeX, 3634 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(590 - playerResizeX, 3634 - playerResizeY, 587,707)]
        for frame in self.walkingFrameR:
            frame.set_colorkey(black)

        self.walkingFrameL = []
        for frame in self.walkingFrameR:
            frame.set_colorkey(black)
            self.walkingFrameL.append(rg.transform.flip(frame, True, False))


        self.jumpingFrameR =[
        self.game.spritesheet.getImage(6480 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(7069 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(1 - playerResizeX, 2216 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(590 - playerResizeX, 2216 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(1179 - playerResizeX, 2216 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(1768 - playerResizeX, 2216 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(2357 - playerResizeX, 2216 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(2946 - playerResizeX, 2216 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(3535 - playerResizeX, 2216 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(5891 - playerResizeX, 1507 - playerResizeY, 587,707)]
        for frame in self.jumpingFrameR:
            frame.set_colorkey(black)

        self.jumpingFrameL = []
        for frame in self.jumpingFrameR:
            frame.set_colorkey(black)
            self.jumpingFrameL.append(rg.transform.flip(frame, True, False))

        self.attackFrameR =[
        self.game.spritesheet.getImage(590 - playerResizeX, 1 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(1179 - playerResizeX, 1 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(1768 - playerResizeX, 1 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(2357 - playerResizeX, 1 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(2946 - playerResizeX, 1 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(3535 - playerResizeX, 1 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(4124 - playerResizeX, 1 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(4713 - playerResizeX, 1 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(5302 - playerResizeX, 1 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(1 - playerResizeX, 1 - playerResizeY, 587,707)]
        for frame in self.attackFrameR:
            frame.set_colorkey(black)

        self.attackFrameL = []
        for frame in self.attackFrameR:
            frame.set_colorkey(black)
            self.attackFrameL.append(rg.transform.flip(frame, True, False))

        self.idleFrameR = [
        self.game.spritesheet.getImage(590 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(1179 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(1768 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(2357 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(2946 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(3535 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(4124 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(4713 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(5302 - playerResizeX, 1507 - playerResizeY, 587,707),
        self.game.spritesheet.getImage(1 - playerResizeX, 1507 - playerResizeY, 587,707)]
        for frame in self.idleFrameR:
            frame.set_colorkey(black)

        self.idleFrameL = []
        for frame in self.idleFrameR:
            frame.set_colorkey(black)
            self.idleFrameL.append(rg.transform.flip(frame, True, False))

    def jump(self):
        #jump on ground only
        if not self.attacking:
            self.rect.y += 1
            hits = rg.sprite.spritecollide(self, self.game.platforms,False)
    #        self.rect.x -= 1
            if hits:
                self.vel.y = -20
            else:
                hits = rg.sprite.spritecollide(self, self.game.ground,False)
                if hits:
                    self.vel.y = -20
            self.rect.y -= 1

    def update(self):
        self.animate()
        self.acc = vec(0, playerGrav)
        keys = rg.key.get_pressed()
        if keys[rg.K_LEFT]:
            self.acc.x = -playerAcc
            self.facing = -1
        if keys[rg.K_RIGHT]:
            self.acc.x  = playerAcc
            self.facing = 1
        if keys[rg.K_p]:
            self.star = True

        # fraction
        self.acc.x += self.vel.x * playerFrict
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.rect.midbottom = self.pos
        self.rcopy = self.rect.copy()
        hit = False
        self.rcopy.x += self.vel.x + 0.5 * self.acc.x
        for p in self.game.platforms:
            if self.rcopy.colliderect(p.rect):
                if self.star:
                    p.kill()
                    self.star = False
                hit = True
                if 0 > self.vel.x + 0.5 * self.acc.x:
                    self.rcopy.left = p.rect.right
                else:
                    self.rcopy.right = p.rect.left
        for p in self.game.ground:
            if self.rcopy.colliderect(p.rect):
                hit = True
                if 0 > self.vel.x + 0.5 * self.acc.x:
                    self.rcopy.left = p.rect.right
                else:
                    self.rcopy.right = p.rect.left
        if hit:
            self.vel.x = 0
            self.acc.x = 0
        hit = False
        self.rcopy.y += self.vel.y + 0.5 * self.acc.y
        for p in self.game.platforms:
            if self.rcopy.colliderect(p.rect):
                hit = True
                if 0 > self.vel.y + 0.5 * self.acc.y:
                    self.rcopy.top = p.rect.bottom
                else:
                    self.rcopy.bottom = p.rect.top
        for p in self.game.ground:
            if self.rcopy.colliderect(p.rect):
                hit = True
                if 0 > self.vel.y + 0.5 * self.acc.y:
                    self.rcopy.top = p.rect.bottom
                else:
                    self.rcopy.bottom = p.rect.top
        if hit:
            self.vel.y = 0
            self.acc.y = 0

        # end of screen
        self.game.offset += self.rcopy.x - (self.rect.x)
        self.pos.y = self.rcopy.midbottom[1]
        self.rect.y = self.rcopy.y


    def animate(self):
        now = rg.time.get_ticks()
        if self.vel.x != 0:
            self.walking = True
        else:
            self.walking = False

        if self.vel.y != 0:
            self.jumping = True
        else:
            self.jumping = False

        keys = rg.key.get_pressed()
        if keys[rg.K_a]:
            if not self.jumping:
                self.attacking = True
        if self.attacking:
            if now - self.lastUpdate > 40:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1)
                if self.currentFrame % len(self.attackFrameR) < self.currentFrame:
                    self.currentFrame = self.currentFrame % len(self.attackFrameR)
                    self.attacking = False
                if self.facing == 1:
                    self.image = self.attackFrameR[self.currentFrame]
                else:
                    self.image = self.attackFrameL[self.currentFrame]
                self.rect = self.image.get_rect()
################################################################################
        if self.attacking:
            pass
        # walking
        elif self.walking and not self.jumping:
            if now - self.lastUpdate > 125:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(self.walkingFrameR)
                bottom = self.rect.bottom
                if self.facing == 1:
                    self.image = self.walkingFrameR[self.currentFrame]
                else:
                    self.image = self.walkingFrameL[self.currentFrame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        # idle
        elif not self.jumping and not self.walking:
            if now - self.lastUpdate > 125:
                self.lastUpdate = now
                self.current_frame = (self.currentFrame + 1) % len(self.idleFrameR)
                bottom = self.rect.bottom
                if self.facing == 1:
                    self.image = self.idleFrameR[self.currentFrame]
                else:
                    self.image = self.idleFrameL[self.currentFrame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom

        # jumping
        elif self.jumping:
            self.walking = False
            if now - self.lastUpdate > 125:
                self.lastUpdate = now
                self.currentFrame = (self.currentFrame + 1) % len(self.walkingFrameR)
                bottom = self.rect.bottom
                if self.facing == 1:
                    self.image = self.jumpingFrameR[self.currentFrame]
                else:
                    self.image = self.jumpingFrameL[self.currentFrame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom


class Enemy(rg.sprite.Sprite):
    def __init__(self, game, x, y):
        rg.sprite.Sprite.__init__(self)
        self.game = game
        self.walking = True
        self.jumping = False
        self.currentFrame = 0
        self.lastUpdate = 0
        self.loadImages()
        self.image = self.walkingFrameL[0]
        self.image.set_colorkey(black)
        self.rect = self.image.get_rect()
#        self.vx = randrange(1,8)
        self.pos = vec(x, y)
        self.rect.left = x - game.offset
        self.rect.bottom = y
#        self.pos = vec(self.rect.x, self.rect.y)
        self.acc = vec(-1 * enemyAcc, enemyGrav)
        self.vel = vec(0, 0)
        self.rcopy = self.rect.copy()

    def loadImages(self):

        self.walkingFrameR = [
        self.game.spritesheet.getImage(7097, 6982 + 350, 885, 707 - 350),
        self.game.spritesheet.getImage(7783,    1 + 350, 885, 707 - 350),
        self.game.spritesheet.getImage(7658,  838 + 350, 885, 835 - 350),
        self.game.spritesheet.getImage(7658, 2512 + 350, 885, 835 - 350),
        self.game.spritesheet.getImage(7658, 3349 + 350, 885, 835 - 350),
        self.game.spritesheet.getImage(7984, 4186 + 350, 885, 835 - 350),
        self.game.spritesheet.getImage(7984, 5023 + 350, 885, 835 - 350)]
        for frame in self.walkingFrameR:
            frame.set_colorkey(black)

        self.walkingFrameL = []
        for frame in self.walkingFrameR:
            frame.set_colorkey(black)
            self.walkingFrameL.append(rg.transform.flip(frame, True, False))


#        self.attackFrameR =[
#        self.game.spritesheet.getImage(590, 1, 587,707),
#        self.game.spritesheet.getImage(1179, 1, 587,707),
#        self.game.spritesheet.getImage(1768, 1, 587,707),
#        self.game.spritesheet.getImage(2357, 1, 587,707),
#        self.game.spritesheet.getImage(2946, 1, 587,707),
#        self.game.spritesheet.getImage(3535, 1, 587,707),
#        self.game.spritesheet.getImage(4124, 1, 587,707),
#        self.game.spritesheet.getImage(4713, 1, 587,707),
#        self.game.spritesheet.getImage(5302, 1, 587,707),
#        self.game.spritesheet.getImage(1, 1, 587,707)]
#        for frame in self.attackFrameR:
#            frame.set_colorkey(black)
#
#        self.attackFrameL = []
#        for frame in self.attackFrameR:
#            frame.set_colorkey(black)
#            self.attackFrameL.append(rg.transform.flip(frame, True, False))

#        self.idleFrame = [
#        self.game.spritesheet.getImage(5323, 6145, 885,835),
#        self.game.spritesheet.getImage(6210, 6145, 885,835),
#        self.game.spritesheet.getImage(7097, 6145, 885,835),
#        self.game.spritesheet.getImage(1, 6982, 885,835),
#        self.game.spritesheet.getImage(888, 6982, 885,835),
#        self.game.spritesheet.getImage(1775, 6982, 885,835),
#        self.game.spritesheet.getImage(3549, 6982, 885,835),
#        self.game.spritesheet.getImage(4436, 6145, 885,835),
#        self.game.spritesheet.getImage(5302, 6982, 885,835),
#        self.game.spritesheet.getImage(5323, 6982, 885,835)]
#        for frame in self.idleFrame:
#            frame.set_colorkey(black)

    def update(self):
        self.animate()
        hit = False
        self.vel += self.acc
        self.vel.x += self.vel.x * enemyFrict
        self.rcopy.x = self.pos.x - self.game.offset
        self.rcopy.x += self.vel.x

        for p in self.game.platforms:
            if self.rcopy.colliderect(p.rect):
                hit = True
                if 0 > self.vel.x + 0.5 * self.acc.x:
                    self.rcopy.left = p.rect.right
                else:
                    self.rcopy.right = p.rect.left
        for p in self.game.ground:
            if self.rcopy.colliderect(p.rect):
                hit = True
                if 0 > self.vel.x + 0.5 * self.acc.x:
                    self.rcopy.left = p.rect.right
                else:
                    self.rcopy.right = p.rect.left
        if hit:
            self.vel.x = 0
            self.acc.x *= -1
        hit = False
        self.rcopy.y += self.vel.y + 0.5 * self.acc.y
        for p in self.game.platforms:
            if self.rcopy.colliderect(p.rect):
                hit = True
                if 0 > self.vel.y + 0.5 * self.acc.y:
                    self.rcopy.top = p.rect.bottom
                else:
                    self.rcopy.bottom = p.rect.top
        for p in self.game.ground:
            if self.rcopy.colliderect(p.rect):
                hit = True
                if 0 > self.vel.y + 0.5 * self.acc.y:
                    self.rcopy.top = p.rect.bottom
                else:
                    self.rcopy.bottom = p.rect.top
        if hit:
            self.vel.y = 0
        self.rect.x = self.rcopy.x
        self.pos.x = self.game.offset + self.rect.x
        self.rect.y = self.rcopy.y

        if self.rect.left > (1.5 * width) or self.rect.right < (-0.5 * width) or self.rect.top > height + 100:
            print('kill enemy', self.game.offset - (2 * width), self.rect.left, self.game.offset + (2 * width))
            self.kill()



    def animate(self):
        now = rg.time.get_ticks()
#        no jumping animation
#        if self.vel.y != 0:
#            self.jumping = True
#        else:
#            self.jumping = False

        if now - self.lastUpdate > 125:
            self.lastUpdate = now
            self.currentFrame = (self.currentFrame + 1) % len(self.walkingFrameR)
            bottom = self.rect.bottom
            # walking
            if not self.jumping:
                    if self.vel.x > 0:
                        self.image = self.walkingFrameR[self.currentFrame]
                    else:
                        self.image = self.walkingFrameL[self.currentFrame]
            else:
                if self.vel.x > 0:
                    self.image = self.jumpingFrameR[self.currentFrame]
                else:
                    self.image = self.jumpingFrameL[self.currentFrame]
            self.rect = self.image.get_rect()
            self.rect.bottom = bottom


class Ground(rg.sprite.Sprite):
    def __init__ (self, game, x, y, w, h):
        super().__init__()
        self.game = game
        self.image = rg.Surface((w,h))
        self.image.fill(lime)
        self.pos = vec(x, y)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y


class Platform(rg.sprite.Sprite):
    def __init__ (self, game, x, y, w, h):
        super().__init__()
        self.game = game
        self.image = rg.Surface((w,h))
        self.image.fill(white)
        self.pos = vec(x,y)
        self.rect = self.image.get_rect()
        self.rect.x = x - self.game.offset
        self.rect.y = y

    def draw(self, screen):
        self.rect.x = self.pos.x - self.game.offset
        super().draw(screen)

    def update(self, *args):
        self.rect.x = self.pos.x - self.game.offset
