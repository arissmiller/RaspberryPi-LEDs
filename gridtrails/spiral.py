import pygame
import math
from axistree import Axistree
from colorfunctions import *
from decayfunctions import *
from gridtrails import *

#draw a wheel of axistrees that fits within the screen
#returns an array of points
def genWheel(screen_width, screen_height, steps_in_radius, rect_width):
    diameter = 0
    if(screen_width <= screen_height):
        diameter = screen_width
    else:
        diamter = screen_height
    centerpoint = Axistree(None, math.floor(screen_height/2), 0, math.floor(screen_width/2))
    radius = diameter / 2
    stepSize = radius / steps_in_radius
    points = []
    #place center points
    for i in range(1, steps_in_radius):
       #add a point on each side of the radius
       radius = i * stepSize
       point1 = Axistree(centerpoint, math.floor(radius), 0,0)
       point2 = Axistree(centerpoint, math.floor(radius), math.radians(180), 0)
       points.append(point1)
       points.append(point2)
    return points

def linear_radius_to_heat(distance, radius):
    return(math.floor(((radius - distance)/radius) * 255))


def heat_to_green(heat):
    limitedHeat = 0
    if(heat > 255):
        limitedHeat = 255
    return(math.floor(limitedHeat/3), limitedHeat, math.floor(limitedHeat/3), math.floor(limitedHeat/3))

def main():
    screen_width = 800
    screen_height = 800
    rect_width = 40
    num_steps = 10

    radius = 0
    if(screen_width < screen_height):
        radius = math.sqrt((screen_width/2)**2 / 2)
    else:
       radius = math.sqrt((screen_height/2)**2/ 2)
    stepSize = math.floor(radius/num_steps)

    screen = pygame.display.set_mode((screen_width, screen_height))

    points = genWheel(screen_width, screen_height, num_steps, rect_width)
    sources = []
    for i in range(0, len(points)):
        sources.append(HeatSource(10, points[i].getCoordinates(), linear_radius_to_heat, colorIce, make_linear_decay_function(1.4)))
    running = True
    stepdirection = 1
    while running:

        screen.fill((0, 0, 15, 255))

        for i in range(0, len(sources)):
            sources[i].giveHeat()
            sources[i].decayHeat()
            sources[i].coords = points[i].getCoordinates()
        level = 0.1
        for point in points:
            point.angle += math.radians(level)
            level += 0.1
        renderHeatSources(screen, sources)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #x = x + 20
        #y = y + 20

if __name__=="__main__":
    main()
