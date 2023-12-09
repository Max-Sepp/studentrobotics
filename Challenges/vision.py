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

            if marker.position.horizontal_angle <= -0.2618:
                robot.kch.leds[LED_A].colour = Colour.YELLOW
            else:
                robot.kch.leds[LED_A].colour = Colour.OFF

            if -0.2618 < marker.position.horizontal_angle < 0.2618:
                robot.kch.leds[LED_B].colour = Colour.YELLOW
            else:
                robot.kch.leds[LED_B].colour = Colour.OFF
            
            if marker.position.horizontal_angle >= 0.2618:
                robot.kch.leds[LED_C].colour = Colour.YELLOW
            else:
                robot.kch.leds[LED_C].colour = Colour.OFF

def Vision_Challenge_Distance():
    while True:
        markers = robot.camera.see()
        for marker in markers:
            print("HA: " +str(marker.position.horizontal_angle))
            print("ASIN: " +str(math.asin(200/marker.position.distance)))
            if marker.position.horizontal_angle > math.asin(200/marker.position.distance):
                robot.kch.leds[LED_C].colour = Colour.BLUE
            else:
                robot.kch.leds[LED_C].colour = Colour.OFF

            if -math.asin(200/marker.position.distance) < marker.position.horizontal_angle < math.asin(200/marker.position.distance):
                robot.kch.leds[LED_B].colour = Colour.YELLOW
            else:
                robot.kch.leds[LED_B].colour = Colour.OFF

            if marker.position.horizontal_angle < -math.asin(200/marker.position.distance):
                robot.kch.leds[LED_A].colour = Colour.BLUE
            else:
                robot.kch.leds[LED_A].colour = Colour.OFF


#Vision_Challenge_Angle()
Vision_Challenge_Distance()