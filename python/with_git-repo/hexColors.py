from random import randint

def hex_colors(numberOfValues):
    hex_values = "0123456789abcdef"
    list_of_hex_colors = []

    for i in range(numberOfValues):
        hex_color = "#"
        for i in range(6):
            hex_color += hex_values[randint(0,15)]

        list_of_hex_colors.append(hex_color)
    return list_of_hex_colors

number = int(input("how many hex color values do you want : "))

print(hex_colors(number))