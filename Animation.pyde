xCoord = random(50,200)
yCoord = random(50,200)
xSpeed = 30
ySpeed = 30
ellipS = 50

def setup():
    size(600,800)
    
def draw():
    background(0)
    global xCoord, yCoord, ySpeed, xSpeed, ellipS
    leftBoundary = ellipS / 2
    rightBoundary = 600 - ellipS / 2
    topBoundary = ellipS / 2
    bottomBoundary = 800 - ellipS / 2
    if yCoord >= bottomBoundary or yCoord <= topBoundary:
        ySpeed = -ySpeed
    if xCoord >= rightBoundary or xCoord <= leftBoundary:
        xSpeed = -xSpeed
    xCoord += xSpeed
    yCoord += ySpeed
    fill(255,0,0)
    ellipse(xCoord,yCoord,ellipS,ellipS)
