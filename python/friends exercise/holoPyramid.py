height = int(input("enter height of the holo pyramid : "))


for i in range(height):
    pattern = "* "*(height-i)
    print(pattern + "  "*2*i + pattern)

