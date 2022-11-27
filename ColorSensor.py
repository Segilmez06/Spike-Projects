from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()
sensor = ColorSensor('E')
motors = MotorPair('C', 'D')

colorlist = []

sensor.wait_until_color('black')

color = ''

while True:

    while color != 'black':
        sensor.light_up_all(100)
        wait_for_seconds(.15)

        color = sensor.wait_for_new_color()
        if color == None:
            continue
        colorlist.append(color)
        print(color)
        sensor.light_up_all(0)
        wait_for_seconds(1)

    for c in colorlist:
        if c == "yellow":
            hub.light_matrix.show_image("ARROW_N")
            motors.move(10, 'cm', 0, 100)
            
        elif c == "red":
            hub.light_matrix.show_image("ARROW_S")
            motors.move(-10, 'cm', 0, 100)
            
        elif c == "green":
            hub.light_matrix.show_image("ARROW_E")
            motors.move(10, 'cm', -100, 100)

        elif c == "violet":
            hub.light_matrix.show_image("ARROW_W")
            motors.move(10, 'cm', 100, 100)

    sensor.wait_until_color('black')
    color = ''
    colorlist = []
