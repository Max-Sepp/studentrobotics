from sr.robot3 import *

robot = Robot()
print(abs(-1))

PI = 3.14159
RadiansConverter = 57.29578


our_qr = [0, 1, 2, 3, 4, 5, 6]

box_qr= []

for i in range (150, 200):
    box_qr.append(i)

def spin():
    robot.motor_boards["srABC1"].motors[0].power = 0.05
    robot.motor_boards["srABC1"].motors[1].power = -0.05
    robot.sleep(0.01)
    robot.motor_boards["srABC1"].motors[0].power = 0
    robot.motor_boards["srABC1"].motors[1].power = 0
    
def align_to_list(qr):
    global RadiansConverter
    repeat = True
    while repeat: 
        print("Spinning:")
        spin() # Spin a bit
        print("Now I'll look for some markers.")
        robot.sleep(0.5)
        markers = robot.camera.see() # THIS LINE NEVER EXECUTES - WHY?
        robot.sleep(0.5)
        print("I've got some markers.")
        print("I see " + str(len(markers)) + " markers.")
        for marker in markers:
            # print("Potential marker: " + str(marker.id) + " at angle " + str(marker.position.horizontal_angle))
            # print(marker.id in qr)
            # print(abs(marker.position.horizontal_angle))
            # print(15*RadiansConverter)
            # print(str(marker.id))
            # print(marker.id in qr and abs(marker.position.horizontal_angle) <= 15*RadiansConverter)
            if marker.id in qr and abs(marker.position.horizontal_angle) <= 15*RadiansConverter:
                print("I like " + str(marker.id))
                return marker.id, marker.position.distance


            
def go_forwards_until_marker( qr):
    markerID, markerDist = align_to_list( qr) # Get a marker to go for
    print("Gunning for marker " + str(markerID))
    robot.motor_boards["srABC1"].motors[0].power = 0.3
    robot.motor_boards["srABC1"].motors[1].power = 0.3
    print("Full steam ahead!")
    if markerDist >= 20:
        print("A way out from marker " + str(markerID))
        while markerDist >= 20:
            print("Going!")
        print("I'm here at marker " + str(markerID))
    else:
        print("Already at marker " + str(markerID))
    print("Stopping!")
    robot.motor_boards["srABC1"].motors[0].power = 0
    robot.motor_boards["srABC1"].motors[1].power = 0
            




print("Let's go to a box.")
go_forwards_until_marker(box_qr)
print("Let's go home.")
go_forwards_until_marker(our_qr)