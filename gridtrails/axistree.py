#axis tree class

#parent at highest level of heirarchy only has x and y offset as coords
#angles are defined clockwise from vertical

import math

class Axistree:
    def __init__(self, parent, radius, angle, xoffset):
        self.parent = parent
        self.radius = radius
        self.angle = angle
        self.xoffset = xoffset

    def getCoordinates(self):
        if(self.parent is None):
            #this axistree has no parent, the coordinates are the x and y xoffset (from the origin)
            return (self.xoffset, self.radius)
        else:
            #determine coordinates based on radius, angle to vertical, x and y offset, and coordinates of parent
            #get coords of parent
            parentcoords = self.parent.getCoordinates()
            #determine the angle to vertical after all parent angles have been applied
            angleFromVertical = self.getAngleFromVertical()
            #find angle to be added to angle from vertical based on x offset
            angleOffset = math.atan(self.xoffset/self.radius)
            if(self.xoffset < 0):
                angleOffset = angleOffset * -1

            angleFromVertical = angleFromVertical + angleOffset

            xCoord = math.floor(self.radius * math.sin(angleFromVertical)) + parentcoords[0]
            yCoord = math.floor(self.radius * math.cos(angleFromVertical)) + parentcoords[1]

            return (xCoord, yCoord)
    def getAngleFromVertical(self):
        if(self.parent is None):
            return 0
        else:
            return self.angle + self.parent.getAngleFromVertical()
