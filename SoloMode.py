"""
TO-DO LIST
 - If near the egg, back up a bit to avoid hitting the pedestal.
 - Add faster speed maybe, though this can introduce errors and requires recalibration of the variables below.
 - Decide whether to put all boxes on the opposite side of the arena in the retrievedBoxes array. This requires a similar process to the robot.zone below.
"""
from sr.robot3 import *
robot = Robot()
 
# We do not know which zone we will start in. When competition mode is activated, we will be able to access the robot.zone variable with
# our starting zone. This can be used to reference which markers on the walls will be our home markers.
 
# zone 0 --> 1 through 6
# zone 1 --> 8 through 12
# zone 2 --> 15 through 19
# zone 3 --> 22 through 26
 
# This is all the code below does, including setting us to 1 through 5 if we're testing in school and not actually in the competition.
 
if robot.mode == COMP:
    if robot.zone == 0:
        homeMarkers = [1, 2, 3, 4, 5]
    elif robot.zone == 1:
        homeMarkers = [8, 9, 10, 11, 12]
    elif robot.zone == 2:
        homeMarkers = [15, 16, 17, 18, 19]
    elif robot.zone == 3:
        homeMarkers = [22, 23, 24, 25, 26]
elif robot.mode == DEV:
    print("This is Development")
    homeMarkers = [1, 2, 3, 4, 5]
 
 
AngleTimeMultiplier = 0.0063556 # Multiply the angle you want to turn IN DEGREES with this value in a robot.sleep() function at 0.5 power
DistanceTimeMultiplier = 1.57 # Multiply distance you want to go IN METRES with this value in a robot.sleep() function at 0.5 power
 
RadiansToDegrees = 1/3.1415 * 180   # Multiply a Radian value by this to get it in Degrees
 
retrievedBoxes = [110, 153, 177] # boxes to NOT go after. 110 is the egg, and the other two are boxes directly behind the pedestal, saving us from hitting said pedestal
                                 # Boxes we've retrieved are also added here to avoid us getting them home then seeing them and trying to grab them again :D
 
def turn(angle):    # turns the specified angle, ensuring it chooses the fastest rotation direction, that being Clockwise for 0 -> 90, and ACW for -90 -> 0
    if angle != 0:
        if angle > 0: # Clockwise
            robot.motor_board.motors[0].power = 0.5
            robot.sleep(abs(angle) * AngleTimeMultiplier)
            robot.motor_board.motors[0].power = 0
            robot.sleep(0.05)
            
        elif angle < 0: # Anti - Clockwise
            robot.motor_board.motors[1].power = 0.5
            robot.sleep(abs(angle) * AngleTimeMultiplier)
            robot.motor_board.motors[1].power = 0
            robot.sleep(0.05)
 
def findClosestBox():   # returns the marker object of the closest box
    markers = robot.camera.see() # List of the markers currently in view
    closestMarker = markers[0]   # Just initialising as something.
    for marker in markers:
        if marker.position.distance < closestMarker.position.distance and marker.id > 27 and (marker.id not in retrievedBoxes): 
            closestMarker = marker # If marker x is closer to us than our current closestMarker, set closestMarker to marker x. Repeat to find the closest box.
            retrievedBoxes.append(closestMarker.id) # Add the closest box to retrievedBoxes to avoid going after it again later.
    return closestMarker
 
def faceBox(closestMarker): # Turns to face a box.
    print("turning to face marker")
    turn(closestMarker.position.horizontal_angle * RadiansToDegrees)
 
def moveToObject(distance, isForwards):  # moves robot to be on top of closest Box
 
    if distance != 0:   # Avoid crashing the programme due to robot.sleep(0) error
 
        if isForwards:          # Forwards or backwards, passed into this function as a respective true, false statement.
            motorPower = 0.5
        else:
            motorPower= -0.5
 
        print("Motors on.")
        robot.motor_board.motors[0].power = motorPower  # zoom forwards / backwards
        robot.motor_board.motors[1].power = motorPower
 
        print("sleeping")
        robot.sleep(abs(distance) / 1000 * 1.57) # / 1000 because distance output by robot is in mm and 
 
        print("motors off")
        robot.motor_board.motors[0].power = 0           # stop zooming
        robot.motor_board.motors[1].power = 0
 
def findClosestHomeMarker(): # returns a home marker object.
    markers = robot.camera.see()    # list of markers in view
 
    facingHome = False
 
    while facingHome == False:  # stopping condition, though the return does this anyway so probably not needed.
 
        for marker in markers:
            print(marker.id)
            if marker.id in homeMarkers:    # if one of the markers in view is a home marker
                facingHome = True
                print("Home marker is marker " + str(marker.id))
                print(marker.id)
                return marker
            
        turn(90)
        markers = robot.camera.see()
        robot.sleep(0.2)
 
def isIdInArray(arr1, arr2):
    for a in arr1:
        if a in arr2:
            return True
    return False
 
def getDistanceToHome():    # Get the distance from current position to a home marker. Should be facing a home marker already if previous function works.
    markers = robot.camera.see()
    for marker in markers:
        if marker.id in homeMarkers:              # If any of the markers we see are a home marker.
            return marker.position.distance - 500 # - 500 to avoid hitting the wall ALTHOUGH we could use this to always face straight by ramming into the flat wall?
 
def enterSoloMode():
 
    while True:
 
        marker = findClosestBox()                       # Find the closest BOX (not wall marker or egg)
        faceBox(marker)                                 # Face towards it
        print("Collecting box " + str(marker.id))
        moveToObject(marker.position.distance - 500, True)    # Move close to it (forwards)
 
        marker = findClosestBox()                       # Ensure we actually go over the box
        faceBox(marker)
        moveToObject(marker.position.distance, True)
 
        faceBox(findClosestHomeMarker())                # findClosestHomeMarker turns in 90 degree increments to find home. faceBox then adjusts this.
        moveToObject(getDistanceToHome(), True)         # move to it (forwards)
        moveToObject(500, False)                        # Move (backwards) to leave egg in our zone
        turn(180)                                       # turn 180 to face the arena again
 
 
 
 
enterSoloMode() # Let the magic begin :D
