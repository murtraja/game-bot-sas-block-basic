import math, time
from pynput.mouse import Button, Controller
mouse = Controller()
centre = (419, 460)
radius = 50
total_points = 16
time_interval_ms = 10


def get_circle_coords(centre, radius, total_points):
    pi = math.pi
    angle_division = 2*pi/total_points
    points = []
    for i in range(total_points):
        x = centre[0] + radius*math.cos(angle_division*i)
        y = centre[1] + radius*math.sin(angle_division*i)
        points.append((x,y))
    return points

points = get_circle_coords(centre, radius, total_points)
i = 0
while True:
    point = points[i]
    i = (i+1)%len(points)
    mouse.position = point
    time.sleep(time_interval_ms/1000)
    
