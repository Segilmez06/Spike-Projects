from spike import *
from spike.control import *
from math import *

hub = PrimeHub()

motors = MotorPair('E', 'A')
lift_motor = Motor('C')
sensor = DistanceSensor('B')

motors.set_default_speed(10)
motors.set_stop_action('coast')
lift_motor.set_default_speed(15)

motors.start()
sensor.wait_for_distance_closer_than(12)
motors.stop()
lift_motor.run_for_degrees(-520)
motors.move(.35, 'rotations', 0, 10)
lift_motor.run_for_degrees(520)
# sensor.wait_for_distance_closer_than(6)
# motors.stop()

# while True:
    # hub.left_button.wait_until_pressed()
    # lift_motor.run_for_degrees(-2)
    # hub.left_button.wait_until_pressed()
    # lift_motor.run_for_degrees(1)
    # hub.left_button.wait_until_pressed()
    # lift_motor.run_for_degrees(520)
    # wait_for_seconds(.5)
    # hub.left_button.wait_until_pressed()
    # lift_motor.run_for_degrees(-25)
    # wait_for_seconds(.5)
