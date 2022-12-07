from spike import *
from spike.control import *
from math import *

platform_algilama_mesafesi = 6
hareket_hizi = 10
kaldirma_hizi = 10

hub = PrimeHub()

motors = MotorPair('E', 'A')
lift_motor = Motor('C')
sensor = DistanceSensor('B')
color = ColorSensor('D')

# motors.set_default_speed(hareket_hizi)
motors.set_stop_action('brake')
lift_motor.set_default_speed(kaldirma_hizi)
lift_motor.set_stop_action('coast')

motors.start(0, 15)

sensor.light_up_all(100)
while color.get_reflected_light() < 95: pass
sensor.light_up_all(0)

motors.stop()
lift_motor.run_for_degrees(-500)
motors.move(.9, 'rotations', 0, 10)
lift_motor.run_for_degrees(500)
# lift_motor.start()
# wait_for_seconds()

motors.move(.66, 'rotations', 100, 10)

motors.start(0, 10)
sensor.wait_for_distance_closer_than(platform_algilama_mesafesi)
lift_motor.start()
motors.stop()

lift_motor.stop()
lift_motor.run_for_degrees(-75)
motors.move(5, 'cm', 0, -10)
motors.move(30, 'cm', 0, -100)
lift_motor.run_for_degrees(80)
