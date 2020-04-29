import pygame as rg
from setting import *
import random
vec = rg.math.Vector2

playerResizeX = 75 - 144
playerResizeY = 30 - 107 + 25

class SpriteSheet:
    def __init__(self, filename):
        self.spritesheet = rg.image.load(filename).convert()

    def getImage(self, x, y, width, height):
        image = rg.Surface((width, height))
        image.blit(self.spritesheet, (0, 0), (x, y, width, height))
        image = rg.transform.scale(image, (width // 5, height // 5))
        return image


class Player(rg.sprite.Sprite):
    def __init__(self, game, ai):
        super().__init__()
        self.game = game
        self.ai = ai
        self.dead = False
        self.walking = False
        self.jumping = False
        self.attacking = False
        self.currentFrame = 0
        self.lastUpdate = 0
        self.walkingFrameR = self.game.walkingFrameR
        self.walkingFrameL = self.game.walkingFrameL
        self.jumpingFrameR = self.game.jumpingFrameR
        self.jumpingFrameL = self.game.jumpingFrameL
        self.attackFrameR = self.game.attackFrameR
        self.attackFrameL = self.game.attackFrameL
        self.idleFrameR = self.game.idleFrameR
        self.idleFrameL = self.game.idleFrameL
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
        self.k_attack = False
        self.k_left = False
        self.k_right = False
        self.k_jump = False
        self.enemies = rg.sprite.Group()
        self.enemyTimer = 0
        self.decay = 100
        self.x = self.pos.x

    def jump(self):
        #jump on ground only
        self.rect.y += 1
        hits = rg.sprite.spritecollide(self, self.game.platforms,False)
        for h in hits:
            # print("test " + str(h.pos) + " (" + str(h.rect.top) + ") : " + str(self.pos) + "(" + str(self.rect.bottom) + ")")
            if -2 < self.rect.bottom - h.rect.top < 2:
                self.vel.y = -20
                # print("Plat " + str(hits[0].pos) + " : " + str(self.pos))
        else:
            hits = rg.sprite.spritecollide(self, self.game.ground,False)
            for h in hits:
                if -2 < self.rect.bottom - h.rect.top < 2:
                    self.vel.y = -20
                    # print("Ground : " + str(self.pos))
        self.rect.y -= 1

    def update(self):
        self.enemies.update()
        if not self.ai:
            keys = rg.key.get_pressed()
            self.k_attack = keys[rg.K_a]
            self.k_left = keys[rg.K_LEFT]
            self.k_right = keys[rg.K_RIGHT]
            self.k_jump = keys[rg.K_SPACE]
        self.animate()
        self.acc = vec(0, playerGrav)
        if self.k_left:
            self.acc.x = -playerAcc
            self.facing = -1
        if self.k_right:
            self.acc.x = playerAcc
            self.facing = 1
        if self.k_jump:
            self.jump()

        # fraction
        self.acc.x += self.vel.x * playerFrict
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.rect.midbottom = self.pos
        self.rect.x = (self.pos.x - self.game.offset) + (width / 2)
        self.rcopy = self.rect.copy()
        hit = False
        self.rcopy.x += self.vel.x + 0.5 * self.acc.x
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
        self.pos.x += self.rcopy.x - (self.rect.x)
        self.pos.y = self.rcopy.midbottom[1]
        # self.rect.x = self.rcopy.x
        self.rect.y = self.rcopy.y

        if self.rect.bottom > height:
            self.dead = True
        if self.x >= self.pos.x:
            self.decay -=1
            if self.decay == 0:
                self.dead = True
        else:
            self.x = self.pos.x
            self.decay = 100
        if self.pos.x > MaxX:
            self.dead = True
        # spawn a enemies?
        now = rg.time.get_ticks()
        if now - self.enemyTimer > 5000 + random.choice([-1000, -500, 0, 500, 1000]):
            self.enemyTimer = now
            e = Enemy(self.game, self.game.offset + width - 1, height - 50)
            self.game.allObjects.add(e)
            self.enemies.add(e)

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
        if self.k_attack:
            self.attacking = True
            self.k_attack = False
            self.lastUpdate = now - 50
            self.currentFrame = -1
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
        self.walkingFrameR = self.game.EwalkingFrameR
        self.walkingFrameL = self.game.EwalkingFrameL
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
            # print('kill enemy', self.game.offset - (2 * width), self.rect.left, self.game.offset + (2 * width))
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
            self.currentFrame = (self.currentFrame + 1) % len(self.walkingFrameL)
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
