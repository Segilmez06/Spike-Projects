from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

bruh = PrimeHub()
sensor = ForceSensor('F')
motors = MotorPair('C','D')
motor = Motor('E')

bruh.left_button.wait_until_pressed()

while True:
    if bruh.right_button.was_pressed():
        motors.stop()
        motor.stop()
        bruh.status_light.on('white')
        bruh.left_button.wait_until_pressed()

    if sensor.is_pressed():
        bruh.light_matrix.show_image('SQUARE')
        bruh.status_light.on('red')
        motors.stop()
        motor.start(100)
        motors.start(0, -100)
        wait_for_seconds(1)
        motors.start(50, 100)
        wait_for_seconds(1)

    else:
        bruh.light_matrix.show_image('ARROW_N')
        bruh.status_light.on('green')
        motors.start(0,100)
        motor.stop()
