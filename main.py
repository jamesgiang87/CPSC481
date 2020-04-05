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
            while len(self.platforms) < 4:
                newWidthSize = random.randrange(100, 200)
                p = Platform(random.randrange( 300, height - 40),
                random.randrange(0, width ), newWidthSize, 20)
                self.platforms.add(p)
                self.allObjects.add(p)
                print('add plat')





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
