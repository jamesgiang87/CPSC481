#importing libraries
import pygame as rg
import random
import os
from setting import *
from spires import *

class Game:
        def __init__(self):
            #init pygame and game window
            rg.init()
            rg.mixer.init()
            self.screen = rg.display.set_mode((width,height))
            rg.display.set_caption("game")
            self.clock = rg.time.Clock()
            self.running = True

        def new(self):
            self.allObjects = rg.sprite.Group()
            self.platforms = rg.sprite.Group()
            self.player = Player(self)
            self.allObjects.add(self.player)
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
            #check if player is falling onto platform
            if self.player.vel.y > 0:
                hits = rg.sprite.spritecollide(self.player,self.platforms,False)
                if hits:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
            #if player is 2/3 of the screen
            if self.player.rect.right <= width / 3:
                self.player.pos.x -= abs(self.player.vel.x)
                for plat in self . platforms:
                    plat.rect.x -= abs(self.player.vel.x)
                    if plat.rect.right >= width:
                        plat.kill()

            # spawn new platformList
            while len(self.platforms) < 6:
                widthPos = random.randrange(50, 100)
                p = Platform(random.randrange(0, width - widthPos),
                random.randrange(20, 30), widthPos, 20)
                self.platforms.add(p)
                self.allObjects.add(p)

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

            pass

        def draw(self):
            #draw screen
            self.screen.fill(black)
            self.allObjects.draw(self.screen)

             #update display double buffer
            rg.display.flip()


        def startScreen(self):
            #start screen
            pass

        def retryScreen(self):
            #game over retry
            pass



g = Game()
g.startScreen()
while g.running:
    g.new()
    g.retryScreen()

rg.quit()
