from sr.robot3 import *
robot = Robot()

# Start
asteroidCount = 0
direction = 0
xPos = 0 # Update these three (direction, xPos, yPos) regularly
yPos = 0 
flapsOpen = True

# Extend arms by 17cm

# Move forward
robotSpeed

# Search for blocks
# Look for specific QR codes (not egg)
# Obstruct camera's field of view (prevent from missing blocks)

# Initalise constants and check qr code value
asteroidQrCodeLow = 150
asteroidQrCodeHi = 199
eggQrCode = 110
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
        # Turn to face home planet

# Kev
