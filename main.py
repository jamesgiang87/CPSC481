#importing libraries
import pygame as rg
import random
import os
from setting import *
from spires import *
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
            self.enemy = rg.sprite.Group()
            #self.allObjects.add(self.enemy)
            self.ground = rg.sprite.Group()
            self.allObjects.add(self.ground)
            for floor in floorList:
                f = Ground(*floor)
                self.allObjects.add(f)
                self.ground.add(f)
            for plat in platformList:
                p = Platform(*plat)
                self.allObjects.add(p)
                self.platforms.add(p)
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
            while len(self.platforms) < 5:
                newWidthSize = random.randrange(100, 200)
                p = Platform(random.randrange( 300, height - 40),
                random.randrange(0, width ), newWidthSize, 20)
                self.platforms.add(p)
                self.allObjects.add(p)
                print('add plat')

            #player dead
            if self.player.rect.bottom > height:
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
