import pygame
import math
#every heat source has a trail, an array of gridpoints indicating heated pixels
#each pixel in the rect is given heat when the heat source touches it
#the rect is removed from the trail when all heats in the rect have decayed to 0
#each rect can be returned as an array of color values

#the gridtrail is a dictionary, keys being coordinates and values being the heat

class HeatSource:
    def __init__(self, radius, coordinates, radiusToHeat, heatToColor, heatDecay):
        self.radius = radius
        self.coords = coordinates
        self.radiusToHeat = radiusToHeat
        self.heatToColor = heatToColor
        self.heatDecay = heatDecay
        self.gridtrail = {}

    def giveHeat(self):
        #give heat to coordinates based on radius to heat, add new gridpoints to gridtrail
        #also increase heat of gridpoints in gridtrail that fall in the radius

        #first, go through the rect defined by the radius of the heat HeatSource
        for i in range (self.coords[0] - self.radius, self.coords[0] + self.radius):
            for j in range (self.coords[1] - self.radius, self.coords[1] + self.radius):
                distanceFromCenter = math.sqrt((i - self.coords[0])**2 + (j - self.coords[1])**2)
                if((i,j) in self.gridtrail):
                    heat = self.gridtrail[(i,j)] + self.radiusToHeat(distanceFromCenter, self.radius)
                    self.gridtrail[i,j] = heat
                else:
                    if(distanceFromCenter < self.radius - 1):
                        heat = self.radiusToHeat(distanceFromCenter, self.radius)
                        self.gridtrail[(i,j)] = heat

    def decayHeat(self):
        keys_to_delete = []
        for key in self.gridtrail:
            self.gridtrail[key] = self.heatDecay(self.gridtrail[key])
            if(self.gridtrail[key] <= 0):
                keys_to_delete.append(key)
        for key in keys_to_delete:
            del self.gridtrail[key]

def renderHeatSources(screen, sources):
    pixelsToUpdate = {}
    for source in sources:
        for key in source.gridtrail:
            calculatedColor = source.heatToColor(source.gridtrail[key])
            if(key in pixelsToUpdate):
                #average color with the color that is in pixelsToUpdate
                oldcolor = pixelsToUpdate[key]

                red = math.floor((calculatedColor[0] + oldcolor[0])/2)
                green = math.floor((calculatedColor[1] + oldcolor[1])/2)
                blue = math.floor((calculatedColor[2] + oldcolor[2])/2)
                alpha = math.floor((calculatedColor[3] + oldcolor[3])/2)
                pixelsToUpdate[key] = (red, green, blue, alpha)
            else:
                pixelsToUpdate[key] = calculatedColor

    for key in pixelsToUpdate:
        color = pixelsToUpdate[key]
        screen.set_at(key, color)
