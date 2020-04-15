Title = "CPSC481"


height = 600
width = 1000


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
bgColor = (0,255,255)
