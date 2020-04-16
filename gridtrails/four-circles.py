import pygame
import math
from axistree import Axistree
from colorfunctions import *
from decayfunctions import *
from gridtrails import *

def main():

        visible_axistree_points = []
        source_points = {}

        screen_width = 800
        screen_height = 800
        pygame.init()

        base = Axistree(None, math.floor(screen_width/2), 0, math.floor(screen_height / 2))
        visible_axistree_points.append((base, 0))
        angle1 = 0
        radius1 = screen_width
        if(screen_width > screen_height):
            radius1 = screen_height

        def linear_radius_to_heat(distance, radius):
            return(math.floor(((radius - distance)/radius) * 255))


        sources = []
        sourcesCounter = 0

        for i in range(0, 4):
            new_point = Axistree(base, math.floor(screen_width/8), math.radians(i * 90), 0)
            for j in range(0, 4):
                new_child = Axistree(new_point, math.floor(screen_width/16), math.radians(j * 90), 0)
                visible_axistree_points.append((new_child, sourcesCounter))
                sourcesCounter += 1
                sources.append(HeatSource(5, new_child.getCoordinates(), linear_radius_to_heat, colorFire, make_linear_decay_function(1.4)))
            visible_axistree_points.append((new_point, sourcesCounter))
            sourcesCounter += 1

            sources.append(HeatSource(5, new_point.getCoordinates(), linear_radius_to_heat, colorIce, make_linear_decay_function(1.8)))
        screen = pygame.display.set_mode((screen_width, screen_height))

        #screen.blit(image, (0, 0))
        #grid = GridSurface(screen, sourcesList)

        pygame.display.flip()
        running = True
        while running:

            for i in range(0, len(visible_axistree_points)):
                point = visible_axistree_points[i][0]
                point.angle = math.radians(math.degrees(point.angle) + 1)
                #pygame.draw.circle(screen, (0,255,0), point.getCoordinates(), 10)
                sources[visible_axistree_points[i][1]].coords = point.getCoordinates()

            screen.fill((0, 0, 25, 255))
            renderHeatSources(screen, sources)
            for source in sources:
                source.giveHeat()
                source.decayHeat()

            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            #x = x + 20
            #y = y + 20
            pygame.time.wait(20)

if __name__=="__main__":
    main()
