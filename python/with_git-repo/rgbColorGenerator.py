from random import randint

def rgb_color_gen():
    red = randint(0,255)
    green = randint(0,255)
    blue = randint(0,255)
    color = "rgb(" + str(red) + "," + str(green) + "," + str(blue) + ")"
    return color

print(rgb_color_gen())