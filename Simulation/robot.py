from gettext import find
from turtle import left
from closestMarkerAndDist import closestMarkerAndDist, findBoundaryMarkers
from sr.robot3 import *

def spin(robot):
    robot.motor_boards["srABC1"].motors[0].power = 0.05
    robot.motor_boards["srABC1"].motors[1].power = -0.05
    robot.sleep(0.01)
    robot.motor_boards["srABC1"].motors[0].power = 0
    robot.motor_boards["srABC1"].motors[1].power = 0
    
def align_to_list(robot, qr):
    while True: 
        print("Spinning:")
        spin(robot) # Spin a bit
        print("Now I'll look for some markers.")
        markers = robot.camera.see() # THIS LINE NEVER EXECUTES - WHY?
        print("I've got some markers.")
        print("I see " + str(len(markers)) + " markers.")
        for marker in markers:
            print("Potential marker: " + str(marker.id) + " at angle " + str(marker.position.horizontal_angle))
            if marker.id in qr and abs(marker.position.horizontal_angle) <= 15/RadiansConverter:
                print("I like " + str(marker.id))
                return marker
            
            
def go_forwards_until_marker(robot, qr):
    marker = align_to_list(robot, qr) # Get a marker to go for
    print("Gunning for marker " + str(marker.id))
    robot.motor_boards["srABC1"].motors[0].power = 0.3
    robot.motor_boards["srABC1"].motors[1].power = 0.3
    print("Full steam ahead!")
    if marker.position.distance >= 20:
        print("A way out from marker " + str(marker.id))
        while marker.position.distance >= 20:
            print("Going!")
        print("I'm here at marker " + str(marker.id))
    else:
        print("Already at marker " + str(marker.id))
    print("Stopping!")
    robot.motor_boards["srABC1"].motors[0].power = 0
    robot.motor_boards["srABC1"].motors[1].power = 0
            



PI = 3.14159
RadiansConverter = 57.29578

robot = Robot()

our_qr = [0, 1, 2, 3, 4, 5, 6]

box_qr= []

for i in range (150, 200):
    box_qr.append(i)

print("Let's go to a box.")
go_forwards_until_marker(robot, box_qr)
print("Let's go home.")
go_forwards_until_marker(robot, our_qr)