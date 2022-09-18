from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

hub = PrimeHub()

def wait():
    wait_for_seconds(1)

while True:
    hub.light_matrix.set_pixel(2, 2, brightness=100)
    wait()
    hub.light_matrix.set_pixel(2, 2, brightness=0)

    for i in range(1, 4):
        for j in range(1, 4):
            hub.light_matrix.set_pixel(i, j, brightness=100)
    wait()
    for i in range(1, 4):
        for j in range(1, 4):
            hub.light_matrix.set_pixel(i, j, brightness=0)
    
    hub.light_matrix.show_image('HEART_SMALL')
    wait()
    hub.light_matrix.show_image('HEART_SMALL', brightness=0)

    hub.light_matrix.show_image('HEART')
    wait()
    hub.light_matrix.show_image('HEART', brightness=0)

    wait()
