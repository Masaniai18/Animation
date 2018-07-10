xCoord = 50
yCoord = 50
speed = 2
yspeed = 2
ellipS = 50

def setup():
    size(400,400)
    
def draw():
    background(0)
    global xCoord, yCoord, yspeed, speed, ellipS
    leftTopBoundary = ellipS / 2
    rightBottomBoundary = 400 - ellipS / 2
    if xCoord >= 400 - rightBottomBoundary or xCoord <= leftTopBoundary:
        speed = -speed
    if yCoord >= rightBottomBoundary or yCoord <= leftTopBoundary:
        yspeed = -yspeed
    xCoord += speed
    yCoord += yspeed
    fill(255,0,0)
    ellipse(xCoord,yCoord,ellipS,ellipS)
