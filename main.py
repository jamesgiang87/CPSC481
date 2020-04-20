#importing libraries
import pygame as rg
import random
import os
from setting import *
from spires import *
from random import choice, randrange
from os import path


#game
class Game:
        def __init__(self):
            #init pygame and game window
            rg.init()
            rg.mixer.init()
            self.screen = rg.display.set_mode((width,height))
            rg.display.set_caption("game")
            self.clock = rg.time.Clock()
            self.running = True
            self.fontName = rg.font.match_font(fontType)
            self.loadData()
            self.offset = width / 2
            self.future_plat = 0

        def loadData(self):
            self.dir = path.dirname(__file__)
            imgDir = path.join(self.dir, 'img')
            #load image
            self.spritesheet = SpriteSheet(path.join(imgDir, spritesheet1))



        def new(self):
            self.score = 0
            self.allObjects = rg.sprite.Group()
            self.platforms = rg.sprite.Group()
            self.player = Player(self)
            self.allObjects.add(self.player)
            self.enemies = rg.sprite.Group()
            self.allObjects.add(self.enemies)
            self.ground = rg.sprite.Group()
            self.allObjects.add(self.ground)
            for floor in floorList:
                f = Ground(self, *floor)
                self.allObjects.add(f)
                self.ground.add(f)
            for plat in platformList:
                p = Platform(self, *plat)
                self.allObjects.add(p)
                self.platforms.add(p)
            self.enemyTimer = 0
            self.run()

        def run(self):
            #game loop
            self.playing = True
            while self.playing:
                self.clock.tick(fps)
                self.events()
                self.update()
                self.draw()


        def update(self):
            #update game
            self.allObjects.update()

            #chech if player is on ground
            if self.player.vel.y > 0:
                hits = rg.sprite.spritecollide(self.player,self.ground,False)
                if hits:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0


            #check if player is falling onto platform
            if self.player.vel.y > 0:
                hits = rg.sprite.spritecollide(self.player,self.platforms,False)
                if hits:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0


            #if player is edge of the screen remove platform
            if self.player.rect.right > width:
                self.player.pos.x += abs(self.player.vel.x)
                for plat in self.platforms:
                    plat.rect.x += abs(self.player.vel.x)
                    if plat.rect.right <= width:
                        plat.kill()
                        print('kill')

            # spawn new platformList
            self.future_plat = 0
            for p in self.platforms:
                if p.rect.right > self.player.pos.x:
                    self.future_plat += 1
            while self.future_plat < 5:
                newWidthSize = random.randrange(100, 200)
                p = Platform(self, self.offset + random.randrange( width, 2 * width), random.randrange(height / 4, 3 * height / 4 ), newWidthSize, 20)
                self.platforms.add(p)
                self.allObjects.add(p)
                self.future_plat += 1
                print('add plat')

            #player dead
            if self.player.rect.bottom > height:
                self.playing = False

        # spawn a enemies?
            now = rg.time.get_ticks()
            if now - self.enemyTimer > 5000 + random.choice([-1000, -500, 0, 500, 1000]):
                self.enemyTimer = now
                e = Enemy(self)
                self.allObjects.add(e)
                print('add enemy')
            # hit enemies
            enemyHits = rg.sprite.spritecollide(self.player, self.enemies, False)
            if enemyHits:
                self.playing = False

        def events(self):
            #events
            for event in rg.event.get():
                #check if exit
                if event.type == rg.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False
                if event.type == rg.KEYDOWN:
                    if event.key == rg.K_SPACE:
                        self.player.jump()



        def draw(self):
            #draw screen
            self.screen.fill(bgColor)
            self.allObjects.draw(self.screen)
            self.drawText(str(self.score), 22, white, width / 2, 15)
            self.drawText(str(self.offset), 22, white, width / 2, 40)

             #update display double buffer
            rg.display.flip()


        def startScreen(self):
            #start screen
            self.screen.fill(bgColor)
            self.drawText(Title, 48, white, width / 2, height / 4)
            self.drawText("Arrows to move, spacebar to jump", 22, white, width / 2, height / 2)
            self.drawText("hit any key to start", 22, white, width / 2, height * 3 / 4)
            rg.display.flip()
            self.waitForKey()

        def gameOverScreen(self):
            #game over retry
            if not self.running:
                return
            self.screen.fill(bgColor)
            self.drawText("Game Over", 48, white, width / 2, height / 4)
            self.drawText("Score: "+ str(self.score), 22, white, width / 2, height / 2)
            self.drawText("try again?", 22, white, width / 2, height * 3 / 4)
            rg.display.flip()
            self.waitForKey()

        def waitForKey(self):
            waiting = True
            while waiting:
                self.clock.tick(fps)
                for event in rg.event.get():
                    if event.type == rg.QUIT:
                        waiting = False
                        self.running = False
                    if event.type == rg.KEYUP:
                        waiting = False


        def drawText(self, text, size, color, x, y):
            font = rg.font.Font(self.fontName, size)
            textSurface = font.render(text, True, color)
            textRect = textSurface.get_rect()
            textRect.midtop = (x,y)
            self.screen.blit(textSurface,textRect)


g = Game()
g.startScreen()
while g.running:
    g.new()
    g.gameOverScreen()

rg.quit()
