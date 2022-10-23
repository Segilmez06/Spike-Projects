from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *
import time

bruh = PrimeHub()

while True:
    bruh.light_matrix.set_pixel(0,4)
    bruh.light_matrix.set_pixel(1,4)
    bruh.left_button.wait_until_pressed()
    first = time.time()
    bruh.light_matrix.off()
    bruh.light_matrix.set_pixel(3,4)
    bruh.light_matrix.set_pixel(4,4)
    bruh.right_button.wait_until_pressed()
    second = time.time()
    bruh.light_matrix.off()
    elapsed = second - first
    bruh.light_matrix.write(elapsed)
    wait_for_seconds(.5)
    bruh.light_matrix.off()
    print(elapsed)
