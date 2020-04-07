#importing libraries
import pygame as rg
import random
import os
from setting import *
from spires import *
from platforms import *


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
            self.enemy = Enemy(self)
            self.allObjects.add(self.enemy)
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

            pass

        def events(self):
            #events
            for event in rg.event.get():
                #check if exit
                if event.type == rg.QUIT:
                    if self.playing:
                        self.playing = False
                    self.running = False

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

        def addwall(self, wall):
            self.allObjects.add(wall)
            self.walls.add(wall)

g = Game()
g.startScreen()
while g.running:
    g.new()
    g.retryScreen()

rg.quit()
