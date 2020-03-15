Title = "CPSC481"

width = 800
height = 600

fps = 60

#player movement
playerAcc = 0.5
playerFrict = -0.12
playerGrav = 0.8

#platforms in a listt
platformList = [(0, height - 40, width, 40),(width / 2 - 50, height * 3 / 4, 100, 20),
                (125,height - 300, 100, 20),
                (350, 200, 100, 20),
                (175, 100, 50, 20)]

#colors
black = (0,0,0)
white = (255,255,255)
enemy = (233,134, 10)
yellow = (255,255,0)
