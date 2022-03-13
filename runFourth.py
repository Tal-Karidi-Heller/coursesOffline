from matplotlib.pyplot import plot
from splines.splineAcc import *

# plot_spline(point0, point1, number, WS, V0, V1, L, FBack, acc, dcc = True)

# plot_spline((0, 0, 90), (44.35, 57, 90), "fourthFirst", 49, 150, 40, 4, True, 50, 30)

# plot_spline((44.35, 57, 0), (105, 66, -3), "fourthSecond", 49, 40, 130, 4, True, 50, 30)

# plot_spline((105, 63.4, 0), (116.74, 59.12, -45), "fourthThird", 44, 25, 7, 3, True, 50, 30)

# plot_spline((109, 63, -21), (95, 63.4, 0), "fourthFourth", 44, -5, -20, -4, False, 50, 30)

plot_spline((95, 63.4, 0), (70, 94, 0), "fourthFifth", 34, -50, -20, -4, False, 33, 20)

plot_spline((70, 94, 0), (90, 94, 0), "fourthSixth", 40, 10, 10, 3, True, 40, 20)

plot_spline((90, 94, 0), (67.166667, 94 , 0), "fourthSeventh", 15, -10, -10, -3, False, 10, 10)
