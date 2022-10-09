"use strict"

from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

bruh = PrimeHub()
# bruh.light_matrix.write('Bruh')

motor_set = MotorPair('C','D')

# motor_set.move(30)
# motor_set.move(20, 'cm', -100)
# motor_set.move(30)
# motor_set.move(20, 'cm', -100)

# motor_set.move(2, 'rotations', -100, 50)
# motor_set.move_tank(20, 'cm', 10, 50)

# motor_set.set_default_speed(100)
# motor_set.move(10, 'cm', 0, None)
# motor_set.set_motor_rotation(27.6, 'cm')
# motor_set.move(30)
# motor_set.set_stop_action('coast')
# motor_set.stop()



radar_motor = Motor('E')

radar_motor.run_to_position(90)
radar_motor.run_to_position(180)
radar_motor.run_to_position(270)


# def led_blink(x, y):
#     bruh.light_matrix.set_pixel(x, y, brightness=100)
#     wait_for_seconds(0.025)
#     bruh.light_matrix.set_pixel(x, y, brightness=0)


# while True:
#     led_blink(0,0)
#     led_blink(1,0)
#     led_blink(2,0)
#     led_blink(3,0)

#     led_blink(4,0)
#     led_blink(4,1)
#     led_blink(4,2)
#     led_blink(4,3)

#     led_blink(4,4)
#     led_blink(3,4)
#     led_blink(2,4)
#     led_blink(1,4)

#     led_blink(0,4)
#     led_blink(0,3)
#     led_blink(0,2)
#     led_blink(0,1)

