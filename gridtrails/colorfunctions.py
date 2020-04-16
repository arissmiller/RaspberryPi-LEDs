import math

def colorIce(heat):
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
    return (red, green, blue, 255)

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

    return(red, green, blue, 255)