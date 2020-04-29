
Title = "CPSC481"


height = 600
width = 1000

MaxX = 20000

fps = 60

#font
fontType ="arial"

#images
spritesheet1 = "spritesheet.png"
#player movement
playerAcc = 1
playerFrict = -0.12
playerGrav = 0.8

#enemy movement
enemyAcc = 0.5
enemyFrict = -0.12
enemyGrav = 0.8
enemyFreq = 5000

#platforms in a list
# platformList = range(100)
# 1000 x 600
platformList = [(800, 400, 100, 20),
                (1000, 300, 100, 20),
                (1500, 400, 100, 20),
                (1850, 300, 50, 20),
                (1900, 200, 50, 20),
                (1975, 100, 50, 20),
                (2250, 400, 50, 20),
                (2400, 400, 50, 20),
                (2500, 400, 50, 20),
                (2600, 400, 50, 20),
                (2800, 300, 50, 20),
                (3000, 300, 50, 20),
                (3050, 250, 50, 20),
                (3100, 200, 50, 20),
                (3150, 150, 50, 20),
                (3200, 100, 50, 20),
                (3750, 500, 50, 20),
                (3800, 400, 50, 20),
                (3850, 300, 50, 20),
                (3900, 200, 50, 20),
                (3950, 100, 50, 20),
                (4000, 200, 50, 20),
                (4050, 300, 50, 20),
                (4100, 400, 50, 20),
                (4150, 500, 50, 20),
                (4200, 450, 50, 20),
                (4250, 400, 50, 20),
                (4300, 350, 50, 20),
                (4350, 300, 50, 20),
                (4400, 250, 50, 20),
                (4450, 200, 50, 20),
                (4500, 150, 50, 20),
                (5000, 450, 100, 20),
                (5200, 150, 50, 20),
                (5500, 200, 50, 20),
                (6000, 300, 50, 20),
                (6500, 200, 50, 20),
                (6600, 300, 50, 20),
                (7000, 200, 50, 20)]

floorList = [(0, height - 40, width, 40)]

#colors
black = (0,0,0)
white = (255,255,255)
enemyCol = (255,0,0)
yellow = (255,255,0)
lime = (0,255,0)
bgColor = (0,255,255)
=======
Title = "CPSC481"


height = 600
width = 1000


fps = 60

#player movement
playerAcc = 1
playerFrict = -0.12
playerGrav = 0.8

#enemy movement
enemyAcc = 2
enemyFrict = -0.12
enemyGrav = 0.8


#platforms in a list
platformList = range(4)
platformList = [(width / 2 - 50, height * 3 / 4, 100, 20),
                (125, height - 300, 100, 20),
                (350, 200, 100, 20),
                (175, 100, 50, 20),(1200, 300, 50, 20)]

floorList = [(0, height - 40, width, 40)]

#colors
black = (0,0,0)
white = (255,255,255)
enemyCol = (255,0,0)
yellow = (255,255,0)
lime = (0,255,0)

