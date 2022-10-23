from spike import PrimeHub, LightMatrix, Button, StatusLight, ForceSensor, MotionSensor, Speaker, ColorSensor, App, DistanceSensor, Motor, MotorPair
from spike.control import wait_for_seconds, wait_until, Timer
from math import *

bruh = PrimeHub()
sensor = ForceSensor('F')

last_pressure = 0
isRunning = True
while isRunning:
    if bruh.right_button.was_pressed():
        isRunning = False

    pressure = sensor.get_force_newton()
    if pressure != last_pressure:
        
        last_pressure = pressure
        note = 44 + int(pressure * (0.79))
        bruh.speaker.beep(note, 0.2)

        if pressure < 10:
            bruh.light_matrix.write(pressure)

        elif pressure == 10:
            bruh.light_matrix.off()
            bruh.light_matrix.set_pixel(0,0)
            bruh.light_matrix.set_pixel(0,1)
            bruh.light_matrix.set_pixel(0,2)
            bruh.light_matrix.set_pixel(0,3)
            bruh.light_matrix.set_pixel(0,4)
            bruh.light_matrix.set_pixel(2,0)
            bruh.light_matrix.set_pixel(2,1)
            bruh.light_matrix.set_pixel(2,2)
            bruh.light_matrix.set_pixel(2,3)
            bruh.light_matrix.set_pixel(2,4)
            bruh.light_matrix.set_pixel(3,0)
            bruh.light_matrix.set_pixel(3,4)
            bruh.light_matrix.set_pixel(4,0)
            bruh.light_matrix.set_pixel(4,1)
            bruh.light_matrix.set_pixel(4,2)
            bruh.light_matrix.set_pixel(4,3)
            bruh.light_matrix.set_pixel(4,4)
