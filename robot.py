from sr.robot3 import *
import math
robot = Robot()

# Functions and procedures
# Check if the robot is in the inside layer of home planet
def atHome():
    return xPos in homeNodes and yPos in homeEdgeY

# Turning from a wall
def turnAway():
    qrCode = 0 # change
    if wallQrCodeLow <= qrCode <= wallQrCodeHi:
        # Turn 45 degrees to the right

        # Repeat if a wall is still seen
        turnAway()

# Return to home planet
def returnHomePlanet():
    # Facing home
    qrCode = 0 # Change
    if leftSideNodes[0]+1 <= qrCode <= leftSideNodes[1] or qrCode == homeCornerLeftX:
        # Turn left 90 degrees
        print("Turning 90 degrees left")
    elif rightSideNodes[1] <= qrCode <= rightSideNodes[0]-1 or qrCode == homeCornerRightX:
        # Turn right 90 degrees
        print("Turning 90 degrees right")
    elif qrCode not in homeNodes:
        # Turn 180 degrees
        print("Turning 180 degrees")
    
    # Moving towards home
    while not atHome():
        # Move forward
        print("Moving forward")



# Start
asteroidCount = 0
direction = 0
xPos = 0 # Update these three (direction, xPos, yPos) regularly
yPos = 0
flapsOpen = True
zone = robot.zone
if zone == 0:
    # Home nodes: 5 closest to centre
    # Side nodes: [Closest to home, furthest from home]
    homeNodes = [1, 2, 3, 4, 5]
    leftSideNodes = [7, 13]
    rightSideNodes = [27, 21]
elif zone == 1:
    homeNodes = [8, 9, 10, 11, 12]
    leftSideNodes = [14, 20]
    rightSideNodes = [6, 0]
elif zone == 2:
    homeNodes = [15, 16, 17, 18, 19]
    leftSideNodes = [21, 27]
    rightSideNodes = [13, 7]
else:
    homeNodes = [22, 23, 24, 25, 26]
    leftSideNodes = [0, 6]
    rightSideNodes = [20, 14]

# Extend arms by 17cm

# Move forward
robotSpeed = 7

# Search for blocks
# Look for specific QR codes (not egg)
# Obstruct camera's field of view (prevent from missing blocks)

# Initalise constants and check qr code value
wallQrCodeLow = 0
wallQrCodeHi = 27
asteroidQrCodeLow = 150
asteroidQrCodeHi = 199
eggQrCode = 110
homeCornerLeftX = homeNodes[0] - 1
homeCornerRightX = homeNodes[4] + 1
homeCornersX = [homeCornerLeftX, homeCornerRightX]
homeEdgeY = [leftSideNodes[0], rightSideNodes[0]]
qrCode = 0 # change

if asteroidQrCodeLow <= qrCode <= asteroidQrCodeHi:
    # Collect asteroid
    # Turn to face the asteroid

    # Move forward to asteroid

    # Grab it

    # Add one to the asteroid count
    asteroidCount += 1

    # Check if two asteroids are collected
    if asteroidCount == 2:
        # Close flaps
        flapsOpen = False

        # Return to home planet
        returnHomePlanet()

elif qrCode == eggQrCode:
    # Close flaps
    flapsOpen = False

    # Face egg and reverse from it
    
    # Turn away from the egg
elif wallQrCodeLow <= qrCode <= wallQrCodeHi:
    turnAway()

# Kev
