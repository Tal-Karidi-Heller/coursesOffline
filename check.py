from splines.splineAcc import *
from math import cos, sin, radians
import matplotlib.pyplot as plt

# plot_spline(point0, point1, number, WS, V0, V1, L, FBack, acc, dcc = True)

points = []
x, y, angle = 0, 0, 0

for i in range(0, 20):
    for point in plot_spline((x, y, i), (x + cos(radians(i)) * 15, y + sin(radians(i)) * 15, i), "a", 40, 1, 1, 3, True, 40, 20):
        points.append(point)

    x += cos(radians(i)) * 15
    y += sin(radians(i)) * 15

plt.figure("x and y"); plt.plot([point['x'] for point in points], [point['y'] for point in points])

plt.show()