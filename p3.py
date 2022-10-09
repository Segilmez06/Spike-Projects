from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

bruh = PrimeHub()
motor_set = MotorPair('C','D')
radar_motor = Motor('E')


motor_set.move(30)
radar_motor.run_for_degrees(90)
motor_set.move(20, 'cm', -100)
motor_set.move(30)
motor_set.move(20, 'cm', -100)
radar_motor.run_for_degrees(-90)
