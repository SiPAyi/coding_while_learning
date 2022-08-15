import os, time
head = '>'
body = '-'

body_part = 20
total_pixels = 124

for i in range(119):
    os.system('clear')
    print(' '*i + body*body_part + head)
    time.sleep(0.01)