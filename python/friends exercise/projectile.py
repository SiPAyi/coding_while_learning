from math import pi, sin, cos


velocity = 5
angle = 45
angle = pi * (angle/180)
gravity = 9.8

	
intial_horizontal_velocity = u_x = velocity * cos(angle)
intial_vertical_velocity = u_y = velocity * sin(angle)
time_of_flight = (2 * intial_vertical_velocity) / gravity


def xDistance(intial_horizontal_velocity, current_t):
	horizontal_distance = intial_horizontal_velocity * current_t
	return horizontal_distance

def yDistance(intial_vertical_velocity, current_t):
	vertical_distance = intial_vertical_velocity*current_t - 0.5*gravity*current_t*current_t
	return vertical_distance

#print(time_of_flight)
    
#for i in range(36):
#	print('* '*75)
	
print('horizontal distance : ', 'vertical distance :')
for i in range(100):
    present_time = time_of_flight*(i/100)
    print(xDistance(u_x, present_time),yDistance(u_y, present_time))


