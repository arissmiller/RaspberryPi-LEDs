import math
import pygame
from axisree import *
from gridtrails import *


#a heat source pattern
#picture a ladder
#each point on the ladder has a horizontal offset from the point above it
#points accelerate toward the center of the ladder as they move left and right on the rungs
#the ladder moves down, off screen as new points are created and added
#this whole ladder can rotate around a center axistree point. This centerpoint defines the coordinates for the
#rest of the ladder

SCREEN_WIDTH = 800
SCREEN_HEIGHT = SCREEN_WIDTH
#note:some rungs will be off screen to keep the continuous effect going
NUM_RUNGS = 20
LADDER_WIDTH = 250
VERTICAL_VELOCITY = 5
#get the amount of distance to move each tick based on the point's distance from the center of the ladder
#the length of the ladder is the diagonal length of the screen
def getPointVelocity(distFromCenter):

#center point is an axistree at the center of the screen
centerpoint = Axistree(None, SCREEN_HEIGHT / 2, 0, SCREEN_WIDTH / 2)

#yellow-white when hotter, gets orange when cooler. Coolest is almost brown.
#kinda brute forced keeping it in range, idk why it sometimes goes out otherwise
def colorFire(heat):
    #gold = rgb(255,215,0)
    #orange = rgb(255,165,0)
    #coral =  	rgb(255,127,80)
    limitedHeat = 0
    if(heat > 255):
        limitedHeat = 255
    else:
        limitedHeat = heat

    red = 255
    greenRatio = heat / 255
    greenRange = 255 - 127
    green = math.floor(greenRatio * greenRange + 127)
    if(green > 255):
        green = 255
    if (green < 0):
        green = 0

    blueRatio = heat / 255
    blueRange = 80
    blue = math.floor(80 - blueRatio * blueRange)
    if(blue > 255):
        blue = 255
    if(blue < 0):
        blue = 0

    return(red, green, blue)

#blue-white when hotter, dark blue when cooler.
def colorIce(heat):
    #not sure how to do the dip with the blue
    #ice = rgb(240,248,255)
    #melt = rgb(173,216,230)
    #water =rgb(30,144,255)
    limitedHeat = 0
    if(heat > 255):
        limitedHeat = 255
    else:
        limitedHeat = heat
    heatRatio = heat / 255

    redRange = 240 - 30
    red =(heatRatio * redRange + 30)
    if(red > 255):
        red = 255
    if(red < 0):
        red = 0

    greenRange = 248 -144
    green = heatRatio * greenRange + 30
    if(green > 255):
        green = 255
    if(green < 0):
        green = 0

    blue = 230

def linear_radius_to_heat(distance, radius):
    return(math.floor(((radius - distance)/radius) * 255))

def long_decay(heat):
    if(heat > 255):
        return 255
    if(heat - 5 < 0):
        return 0
    return heat - 5
def short_decay(heat):
    return(math.floor(heat/2))

#outerpoints will be axistrees generated as children of the center point
leftpoints = []
rightpoints = []
total_length = math.floor(math.sqrt(SCREEN_WIDTH**2 + SCREEN_HEIGHT**2))
step_size = total_length / NUM_RUNGS
for i in range(0, NUM_RUNGS):
    xoffset = 0
    if i < NUM_RUNGS / 2:
        xoffset = (total_length / 2) - i * step_size
    if i > NUM_RUNGS / 2:
        xoffset = -1*((total_length / 2) - i * step_size)
    leftpoint = Axistree(centerpoint, LADDER_WIDTH / 2, math.radians(-90), xoffset)
    rightpoint = Axistree(centerpoint, LADDER_WIDTH / 2, math.radians(-90), xoffset)
    leftpoints.append(leftpoint)
    rightpoints.append(rightpoint)


#each point in outerpoints gets a heat source
leftheatsources = []
rightheatsources = []
for i in range(0, len(leftpoints)):
    leftheatsources.append(Heatsource(10, leftpoints[i].getCoordinates(), color_Fire, long_decay))
    rightheatsources.append(HeatSource(10, leftpoints[i].getCoordinates(), color_Ice, long_decay))


#each iteration, each point in outer points is moved horizontally and vertically by each velocity.
#there are extra rungs that go off the screen so that the ladder can rotate without ever ending on screen
#once the bottom point goes one rung length, it is moved to one rung length above the top
screen = pygame.display.set_mode((SCREEN_WIDTH, screen_height))

pygame.display.flip()
running = True

while running:
    screen.fill((0, 128, 0, 255))
    for source in sources:
        source.giveHeat()
        source.decayHeat()
        renderHeatSources(screen, sources)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 running = False

if __name__=="__main__":
    main()

#have one heat to color function for each side of the ladder,
#the colors cross over in the center
