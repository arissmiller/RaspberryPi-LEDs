import pygame
import math
from axistree import Axistree
from gridtrails import *

def main():
        screen_width = 800
        screen_height = 800
        pygame.init()

        visible_axistree_points = []
        source_points = {}

        #moving the base point will move everything else
        base = Axistree(None, math.floor(screen_height/3), 0, math.floor(screen_width/3))
        arm1 = Axistree(base, math.floor(screen_height/3), 0, 0)
        arm2 = Axistree(base, math.floor(screen_height/3), 0, math.floor(screen_width/3))
        arm3 = Axistree(base, 0, 0, math.floor(screen_width/3))


        planet1 = Axistree(base, math.floor(screen_height/6), 0, 0)
        planet2 = Axistree(arm1, math.floor(screen_height/6), 0, 0)
        planet3 = Axistree(arm2, math.floor(screen_height/6), 0, 0)
        planet4 = Axistree(arm3, math.floor(screen_height/6), 0, 0)
        planet5 = Axistree(base, math.floor(screen_height/6), math.radians(180), 0)
        planet6 = Axistree(arm1, math.floor(screen_height/6), math.radians(180), 0)
        planet7 = Axistree(arm2, math.floor(screen_height/6), math.radians(180), 0)
        planet8 = Axistree(arm3, math.floor(screen_height/6), math.radians(180), 0)

        #adding the planets to an array so we can set all their angles easily
        planets_array = []
        planets_array.append(planet1)
        planets_array.append(planet2)
        planets_array.append(planet3)
        planets_array.append(planet4)
        planets_array.append(planet5)
        planets_array.append(planet6)
        planets_array.append(planet7)
        planets_array.append(planet8)


        visible_axistree_points.append((base, 0))
        visible_axistree_points.append((arm1, 1))
        visible_axistree_points.append((arm2, 2))
        visible_axistree_points.append((arm3, 3))
        visible_axistree_points.append((planet1, 4))
        visible_axistree_points.append((planet2, 5))
        visible_axistree_points.append((planet3, 6))
        visible_axistree_points.append((planet4, 7))
        visible_axistree_points.append((planet5, 8))
        visible_axistree_points.append((planet6, 9))
        visible_axistree_points.append((planet7, 10))
        visible_axistree_points.append((planet8, 11))


        def linear_radius_to_heat(distance, radius):
            return(math.floor(((radius - distance)/radius) * 255))

        def heat_to_green(heat):
            limitedHeat = 0
            if(heat >= 255):
                limitedHeat = 255
            elif(heat < 0):
                limitedHeat = 0
            else:
                limitedHeat = heat
            return(math.floor(limitedHeat/3), limitedHeat, math.floor(limitedHeat/3), math.floor(limitedHeat/3))
            #return (128, 128, 128, 128)
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

        def heat_to_yellow(heat):
            limitedHeat = 0
            if(heat > 255):
                limitedHeat = 255

            return(limitedHeat, limitedHeat, math.floor(limitedHeat/3), math.floor(limitedHeat/3))
            #return (128, 128, 128, 128)
        def long_decay(heat):
            if(heat > 255):
                return 255
            if(heat - 5 < 0):
                return 0
            return heat - 5
        def short_decay(heat):
            return(math.floor(heat/2))
        sources = []

        for i in range(0, len(visible_axistree_points)):
            sources.append(HeatSource(5, visible_axistree_points[i][0].getCoordinates(), linear_radius_to_heat, color_Fire, long_decay))

        screen = pygame.display.set_mode((screen_width, screen_height))

        #screen.blit(image, (0, 0))
        #grid = GridSurface(screen, sourcesList)

        pygame.display.flip()
        running = True
        initial_base_coordinates = base.getCoordinates()

        stepsize = 3
        xsteps = 0
        ysteps = 0
        xdir = 1
        ydir = -1

        while running:
            base.angle += 3

            for i in range(0, len(visible_axistree_points)):
                point = visible_axistree_points[i][0]
                if(i == 0):
                    #this is the base point
                    if(xsteps == 10):
                        #increment y direction
                        point.radius += stepsize * ydir
                        ysteps += 1
                        if(ysteps == 10):
                            ydir = -1 * ydir
                            #start stepping x backward
                            xdir = -1*xdir
                            point.xoffset += stepsize * xdir
                            xsteps = 1
                    else:
                        ysteps = 0
                        #increment x direction
                        point.xoffset += stepsize * xdir
                        xsteps += 1


                if point in planets_array:
                    point.angle = math.radians(math.degrees(point.angle) + 1)
                #pygame.draw.circle(screen, (0,255,0), point.getCoordinates(), 10)
                #print(len(sources[visible_axistree_points[i][1]].gridtrail))
                sources[visible_axistree_points[i][1]].coords = point.getCoordinates()


            screen.fill((0, 128, 0, 255))

            for source in sources:
                source.giveHeat()
                source.decayHeat()
            renderHeatSources(screen, sources)
            pygame.display.flip()



            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #x = x + 20
            #y = y + 20
            pygame.time.wait(20)

if __name__=="__main__":
    main()
