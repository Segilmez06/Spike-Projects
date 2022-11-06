from spike import PrimeHub, LightMatrix

bruh = PrimeHub()

lightmap = {
    "up": "ARROW_N",
    "down": "ARROW_S",
    "rightside": "ARROW_E",
    "leftside": "ARROW_W",
    "front": "SQUARE_SMALL",
    "back": "SQUARE"
}

while True:
    face = bruh.motion_sensor.get_orientation()
    bruh.light_matrix.show_image(str(lightmap[face]))
