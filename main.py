#importing libraries
import os
from os import path
import neat
from spires import *

rg.font.init()


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
            self.gen = 0
            self.p = [0, 0, 0, 0]
            self.best = width / 2
            self.lastbest = width / 2


        def loadData(self):
            self.dir = path.dirname(__file__)
            imgDir = path.join(self.dir, 'img')
            #load image
            self.spritesheet = SpriteSheet(path.join(imgDir, spritesheet1))
            pHeight = 640
            pWidth = 500
            self.walkingFrameR = [
                self.spritesheet.getImage(1179 - playerResizeX, 3634 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(1768 - playerResizeX, 3634 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(2357 - playerResizeX, 3634 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(2946 - playerResizeX, 3634 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(3535 - playerResizeX, 3634 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(4124 - playerResizeX, 3634 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(4713 - playerResizeX, 3634 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(5302 - playerResizeX, 3634 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(5891 - playerResizeX, 3634 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(590 - playerResizeX, 3634 - playerResizeY, pWidth, pHeight)]
            for frame in self.walkingFrameR:
                frame.set_colorkey(black)

            self.walkingFrameL = []
            for frame in self.walkingFrameR:
                frame.set_colorkey(black)
                self.walkingFrameL.append(rg.transform.flip(frame, True, False))

            self.jumpingFrameR = [
                self.spritesheet.getImage(6480 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(7069 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(1 - playerResizeX, 2216 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(590 - playerResizeX, 2216 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(1179 - playerResizeX, 2216 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(1768 - playerResizeX, 2216 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(2357 - playerResizeX, 2216 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(2946 - playerResizeX, 2216 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(3535 - playerResizeX, 2216 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(5891 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight)]
            for frame in self.jumpingFrameR:
                frame.set_colorkey(black)

            self.jumpingFrameL = []
            for frame in self.jumpingFrameR:
                frame.set_colorkey(black)
                self.jumpingFrameL.append(rg.transform.flip(frame, True, False))

            self.attackFrameR = [
                self.spritesheet.getImage(590 - playerResizeX, 1 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(1179 - playerResizeX, 1 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(1768 - playerResizeX, 1 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(2357 - playerResizeX, 1 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(2946 - playerResizeX, 1 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(3535 - playerResizeX, 1 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(4124 - playerResizeX, 1 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(4713 - playerResizeX, 1 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(5302 - playerResizeX, 1 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(1 - playerResizeX, 1 - playerResizeY, pWidth, pHeight)]
            for frame in self.attackFrameR:
                frame.set_colorkey(black)

            self.attackFrameL = []
            for frame in self.attackFrameR:
                frame.set_colorkey(black)
                self.attackFrameL.append(rg.transform.flip(frame, True, False))

            self.idleFrameR = [
                self.spritesheet.getImage(590 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(1179 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(1768 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(2357 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(2946 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(3535 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(4124 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(4713 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(5302 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight),
                self.spritesheet.getImage(1 - playerResizeX, 1507 - playerResizeY, pWidth, pHeight)]
            for frame in self.idleFrameR:
                frame.set_colorkey(black)

            self.idleFrameL = []
            for frame in self.idleFrameR:
                frame.set_colorkey(black)
                self.idleFrameL.append(rg.transform.flip(frame, True, False))

            self.EwalkingFrameR = [
                self.spritesheet.getImage(7097, 6982 + 350, 885, 707 - 350),
                self.spritesheet.getImage(7783, 1 + 350, 885, 707 - 350),
                self.spritesheet.getImage(7658, 838 + 350, 885, 835 - 350),
                self.spritesheet.getImage(7658, 2512 + 350, 885, 835 - 350),
                self.spritesheet.getImage(7658, 3349 + 350, 885, 835 - 350),
                self.spritesheet.getImage(7984, 4186 + 350, 885, 835 - 350),
                self.spritesheet.getImage(7984, 5023 + 350, 885, 835 - 350)]
            for frame in self.EwalkingFrameR:
                frame.set_colorkey(black)

            self.EwalkingFrameL = []
            for frame in self.EwalkingFrameR:
                frame.set_colorkey(black)
                self.EwalkingFrameL.append(rg.transform.flip(frame, True, False))

        def new(self, genomes, config):
            self.gen += 1
            self.allObjects = rg.sprite.Group()
            self.platforms = rg.sprite.Group()
            self.offset = width / 2
            self.nets = [] # networks
            self.player = []
            self.knights = rg.sprite.Group()
            self.ge = [] # genomes
            for genome_id, genome in genomes:
                genome.fitness = 0
                net = neat.nn.FeedForwardNetwork.create(genome, config)
                self.nets.append(net)
                k = Player(self, True)
                self.player.append(k)
                self.knights.add(k)
                self.ge.append(genome)
#            for p in self.player:
#                self.allObjects.add(p)
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

            self.run()
            self.lastbest = self.offset

        def run(self):
            #game loop
            self.playing = self.running
            while self.playing:
                for x, player in enumerate(self.player):
                    self.ge[x].fitness = player.pos.x
                    x = player.pos.x
                    y = player.pos.y
                    a = []
                    for e in player.enemies:
                        a.append(e.pos.x)
                        a.append(e.pos.y)
                    a.append(0)
                    a.append(0)
                    a.append(0)
                    a.append(0)

                    output = self.nets[self.player.index(player)].activate((player.pos.y, a[0] - player.pos.x, a[1], a[2] - player.pos.x, a[3], self.p[0] - player.pos.x, self.p[1], self.p[2] - player.pos.x, self.p[3]))
                    if output[0] > 0.5:
                        player.k_attack = True
                    else:
                        player.k_attack = False
                    if output[1] > 0.5:
                        player.k_jump = True
                    else:
                        player.k_jump = False
                    if output[2] > 0.5:
                        player.k_right = True
                    else:
                        player.k_right = False
                    if output[2] < -0.5:
                        player.k_left = True
                    else:
                        player.k_left = False
                    player.update()

                self.clock.tick(fps)
                self.events()
                self.update()
                self.draw()


        def update(self):
            # update game
            self.allObjects.update()

            # spawn new platformList
            self.future_plat = 0
            self.p = []
            for p in self.platforms:
                if p.pos.x + p.rect.width > self.offset:
                    self.future_plat += 1
                    self.p.append(p.pos.x)
                    self.p.append(p.pos.y)
            self.p.append(0)
            self.p.append(0)
            self.p.append(0)
            self.p.append(0)
            while self.future_plat < 5:
                newWidthSize = random.randrange(50, 100)
                p = Platform(self, self.offset + random.choice([1, 1.25, 1.5]) * width, random.choice([0.25, 0.5, 0.75]) * height, newWidthSize, 20)
                self.platforms.add(p)
                self.allObjects.add(p)
                self.future_plat += 1
                # print('add plat')
            # hit enemies
            for p in self.player:
                a = False
                if p.attacking:
                    f = p.currentFrame / len(p.attackFrameL)
                    if 0.2 <= f <= 0.8:
                        a = True
                enemyHits = rg.sprite.spritecollide(p, p.enemies, a)
                if (p.pos.x + width < self.offset) or (not a and len(enemyHits) > 0):
                    p.dead = True
                elif p.pos.x > self.offset:
                    self.offset = p.pos.x
                    if self.offset > self.best:
                        self.best = self.offset
                if p.dead:
                    id = self.player.index(p)
                    self.ge[id].fitness = p.pos.x
                    self.nets.pop(id)
                    self.ge.pop(id)
                    if len(self.player) > 1:
                        self.player.pop(self.player.index(p))
                    else:
                        self.playing = False #
                    p.kill()
            if len(self.player) == 0:
                self.playing = False

        def events(self):
            #events
            for event in rg.event.get():
                #check if exit
                if event.type == rg.QUIT:
                    self.playing = False
                    self.running = False



        def draw(self):
            #draw screen
            self.screen.fill(bgColor)
            self.knights.draw(self.screen)
            self.allObjects.draw(self.screen)
            # self.drawText(str(self.players[0].score), 22, white, width / 2, 15)
            self.drawText('Score: {!s}'.format(self.offset), 22, white, width / 2, 15)  # 40
            self.drawText('Generation: {!s}'.format(self.gen), 22, white, width / 2, 40)  # 40
            self.drawText('Knights: {!s}'.format(len(self.player)), 22, white, width / 2, 65)  # 40

            self.drawText('Score: {!s}'.format(self.offset), 22, white, width / 2, 15)  # 40
            self.drawText('Generation: {!s}'.format(self.gen), 22, white, width / 2, 40)  # 40

             #update display double buffer
            rg.display.flip()


        def startScreen(self):
            #start screen
            self.screen.fill(bgColor)
            self.drawText(Title, 48, white, width / 2, height / 4)
            #self.drawText("Arrows to move, spacebar to jump", 22, white, width / 2, height / 2)
            self.drawText("The AI will move the knight(s) left, right, jump and attack", 22, white, width / 2, height / 2)
            self.drawText("hit any key to start", 22, white, width / 2, height * 3 / 4)
            rg.display.flip()
            self.waitForKey()

        def gameOverScreen(self, winner):
            #game over retry
            if not self.running:
                return
            self.screen.fill(bgColor)
            self.drawText("Game Over", 48, white, width / 2, height / 4)
            self.drawText('Generation: {!s}'.format(self.gen), 22, white, width / 2, height / 2)
            print('\nBest genome:\n{!s}'.format(winner))
            self.drawText('Best genome: {!s}'.format(g.best), 22, white, width / 2, height * 3 / 4)
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


def run(config_file, game):
    """
    runs the NEAT algorithm to train a neural network to play flappy bird.
    :param config_file: location of config file
    :return: None
    """
    config = neat.config.Config(neat.DefaultGenome, neat.DefaultReproduction,
                         neat.DefaultSpeciesSet, neat.DefaultStagnation,
                         config_file)

    # Create the population, which is the top-level object for a NEAT run.
    p = neat.Population(config)

    # Add a stdout reporter to show progress in the terminal.
    p.add_reporter(neat.StdOutReporter(True))
    stats = neat.StatisticsReporter()
    p.add_reporter(stats)
    #p.add_reporter(neat.Checkpointer(5))

    # Run for up to 50 generations.
    winner = p.run(g.new, 50) # eval_genomes, 50)

    # show final stats
    return winner


if __name__ == '__main__':
    # Determine path to configuration file. This path manipulation is
    # here so that the script will run successfully regardless of the
    # current working directory.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config-feedforward.txt')
    g = Game()
    g.startScreen()
    winner = run(config_path, g)
    g.gameOverScreen(winner)
    rg.quit()