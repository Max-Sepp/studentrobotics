from sr.robot3 import *
import math
robot = Robot()

def Vision_Challenge_Angle():
    while True:
        markers = robot.camera.see()
        for marker in markers:
            print("Marker #{0} is {1} metres away".format(marker.id,
            marker.position.distance / 1000))

            if marker.position.distance > 1:
                robot.camera.save(robot.usbkey / "initial-view.jpg")

            if marker.horizontal_angle <= -0.2618:
                robot.kch.leds[LED_A].colour = Colour.YELLOW
            else:
                robot.kch.leds[LED_A].colour = Colour.OFF

            if -0.2618 < marker.horizontal_angle < 0.2618:
                robot.kch.leds[LED_B].colour = Colour.YELLOW
            else:
                robot.kch.leds[LED_B].colour = Colour.OFF
            
            if marker.horizontal_angle >= 0.2618:
                robot.kch.leds[LED_C].colour = Colour.YELLOW
            else:
                robot.kch.leds[LED_C].colour = Colour.OFF

def Vision_Challenge_Distance():

    if marker.horizontal_angle > math.atan(0.2/distance):
        robot.kch.leds[LED_C].colour = Colour.BLUE
    else:
        robot.kch.leds[LED_C].colour = Colour.OFF

    if marker.horizontal_angle > -math.atan(0.2/distance) and marker.horizontal_angle < math.atan(0.2/distance):
        robot.kch.leds[LED_B].colour = Colour.YELLOW
    else:
        robot.kch.leds[LED_B].colour = Colour.OFF

    if marker.horizontal_angle < -math.atan(0.2/distance):
        robot.kch.leds[LED_A].colour = Colour.BLUE
    else:
        robot.kch.leds[LED_A].colour = Colour.OFF
        

"""
while True:
    markers = robot.camera.see()
    
    Vision_Challenge_Angle(markers)
"""

Vision_Challenge_Angle()