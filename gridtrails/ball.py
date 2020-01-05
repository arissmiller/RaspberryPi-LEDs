import pygame
import math
from axistree import Axistree
from gridtrails import *

def main():
        pygame.init()

        #logo = pygame.image.load("logo32x32.png")
        #pygame.display.set_icon(logo)
        #pygame.display.set_caption("minimal program")
        image = pygame.image.load("pygame-logo.png")

        base = Axistree(None, 400, 0, 400)
        child1 = Axistree(base, 200, 0, 0)
        child2 = Axistree(child1, 50, 0, 0)
        child3 = Axistree(base, -200, 0, 0)
        child4 = Axistree(child3, 50, 0, 0)

        def radiusToHeat(dist, radius):
            return math.floor(((radius - dist)/radius) * 255)
        def heatDecay(heat):
            return math.floor((heat / 1.2))
        def heatToColor(heat):
            if(heat > 255):
                heat = 255
            ratiored = heat/255
            ratiogreen = (heat/2)/255
            ratioblue = (heat/3)/255
            red = math.floor(255 * ratiored)
            green = math.floor(255 * ratiogreen)
            blue = math.floor(255 * ratioblue)#math.floor(heat / 100 * 255)
            alpha = heat
            return (red, green, blue, alpha)

        source1 = HeatSource(10, base.getCoordinates(), radiusToHeat, heatToColor, heatDecay)
        source2 = HeatSource(10, child1.getCoordinates(), radiusToHeat, heatToColor, heatDecay)
        source3 = HeatSource(10, child2.getCoordinates(), radiusToHeat, heatToColor, heatDecay)
        source4 = HeatSource(10, child3.getCoordinates(), radiusToHeat, heatToColor, heatDecay)
        source5 = HeatSource(10, child4.getCoordinates(), radiusToHeat, heatToColor, heatDecay)

        sourcesList = []
        sourcesList.append(source1)
        sourcesList.append(source2)
        sourcesList.append(source3)
        sourcesList.append(source4)
        sourcesList.append(source5)

        screen = pygame.display.set_mode((800, 800))
        screen.fill((255, 128, 128))
        #screen.blit(image, (0, 0))
        #grid = GridSurface(screen, sourcesList)

        pygame.display.flip()

        running = True
        x = 0
        y = 0
        child1angleDegrees = 0
        child2angleDegrees = 0
        while running:
            screen.fill((255, 128, 128))
            #screen.blit(image,(x, y))
            child1.angle = math.radians(child1angleDegrees)
            child2.angle = math.radians(child2angleDegrees)
            child3.angle = math.radians(child1angleDegrees)
            child4.angle = math.radians(child2angleDegrees)
            source1.coords = base.getCoordinates()
            source2.coords = child1.getCoordinates()
            source3.coords = child2.getCoordinates()
            source4.coords = child3.getCoordinates()
            source5.coords = child4.getCoordinates()
            for source in sourcesList:
                source.decayHeat()
                source.giveHeat()
            #pygame.draw.circle(screen, (0, 255, 0), base.getCoordinates(), 10)
            #pygame.draw.circle(screen, (0, 0, 255), child1.getCoordinates(), 10)
            #pygame.draw.circle(screen, (255, 0, 0), child2.getCoordinates(), 10)
            #pygame.draw.circle(screen, (0, 0, 255), child3.getCoordinates(), 10)
            renderHeatSources(screen, sourcesList)
            pygame.display.flip()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            child1angleDegrees = child1angleDegrees + 2
            child2angleDegrees = child2angleDegrees + 10
            #x = x + 20
            #y = y + 20
            pygame.time.wait(20)

if __name__=="__main__":
    main()
