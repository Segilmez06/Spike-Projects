from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

bruh = PrimeHub()

bruh.light_matrix.write('Bruh')

def led_blink(x, y):
    bruh.light_matrix.set_pixel(x, y, brightness=100)
    wait_for_seconds(0.1)
    bruh.light_matrix.set_pixel(x, y, brightness=0)


while True:
    led_blink(0,0)
    led_blink(1,0)
    led_blink(2,0)
    led_blink(3,0)

    led_blink(4,0)
    led_blink(4,1)
    led_blink(4,2)
    led_blink(4,3)

    led_blink(4,4)
    led_blink(3,4)
    led_blink(2,4)
    led_blink(1,4)

    led_blink(0,4)
    led_blink(0,3)
    led_blink(0,2)
    led_blink(0,1)

    led_blink(1,1)
    led_blink(2,1)

    led_blink(3,1)
    led_blink(3,2)

    led_blink(3,3)
    led_blink(2,3)

    led_blink(1,3)
    led_blink(1,2)
