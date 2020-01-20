import pygame
import math
from axistree import Axistree

#create a stack of rectangles, along an axis, with changing x offset

#divide axis into a number of rectangles
#rectangles stack rotates around center
#rectangles move in x offset, more the farther out on the stack

#draw a rectangle from a center point defined by an axistree
def drawRectangle(axistree, width, height, screen, color):
    center = axistree.getCoordinates()
    xo1 = math.cos(axistree.angle) * (width/2)
    yo1 = math.sin(axistree.angle) * (width/2)

    lcenter = (center[0] - xo1, center[1] + yo1)
    rcenter = (center[1] + xo1, center[1] - yo1)

    xo2 = math.sin(axistree.angle) * (height/2)
    yo2 = math.sin(axistree.angle) * (height/2)

    topleft = (lcenter[0] + xo2, lcenter[1] - yo2)
    bottomleft = (lcenter[0] - xo2, lcenter[1] - yo2)
    topright = (rcenter[0] - xo2, rcenter[1] + yo2)
    bottomright = (rcenter[0] + xo2, rcenter[1] - yo2)

    pygame.draw.polygon(screen, color, [topleft, bottomleft, topright, bottomright])

#draw a wheel of axistrees that fits within the screen
#returns an array of points
def genWheel(screen_width, screen_height, steps_in_radius):
       centerpoint = Axistree(None, screen_height/2, 0, screen_width/2)
       radius = 0
       if(screen_width < screen_height):
           radius = math.sqrt((screen_width/2)**2 / 2)
       else:
           radius = math.sqrt((screen_height/2)**2/ 2)
       stepSize = math.floor(radius/steps_in_radius)

       points = []
       #place center points
       for i in range(0, steps_in_radius):
           #add a point on each side of the radius
           radius = i * stepSize + stepSize / 2
           point1 = Axistree(centerpoint, radius, 0, 0)
           #does this keep points 1 and 2 always at 180 degrees from each other?
           point2 = Axistree(centerpoint, radius, point1.angle + math.radians(180), 0)
           points.append(point1)
           points.append(point2)
       return points

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

    points = genWheel(screen_width, screen_height, num_steps)

    running = True
    while running:

        screen.fill((0, 128, 0, 255))
        for point in points:
            drawRectangle(point, 40, stepSize, screen, (255, 0, 0))
            point.angle += math.radians(3)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        #x = x + 20
        #y = y + 20
        pygame.time.wait(20)

if __name__=="__main__":
    main()
