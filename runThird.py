from splines.splineAcc import *

# plot_spline(point0, point1, number, WS, V0, V1, L, FBack, acc, dcc = True)

plot_spline((0, 0, 90), (46.35, 56, 0), "thirdFirst", 49, 90, 30, 4, True, 50, 30)

plot_spline((46.35, 56, 0), (116, 54.5, -65), "thirdSecond", 47, 140, 10, 4, True, 50, 30)

plot_spline((116, 54.5, -65), (118.747, 48.608, -65), "thirdThird", 40, 5, 5, 4, True, 40, 30)

plot_spline((118.747, 50.108, -65), (116, 56, -45), "thirdThirdHalf", 40, -5, -5, -4, False, 40, 30)

plot_spline((116, 56, 0), (161.747, 87.108, 45), "thirdFourth", 40, 30, 90, 4, True, 40, 30)

plot_spline((161.747, 87.108, 45), (160.332, 85.693, 45), "thirdFifth", 40, -5, -5, -3, False, 40, 30)

plot_spline((160.332, 85.693, 90), (160.332, 50, 90), "thirdSixth", 40, -10, -10, -4, False, 40, 25)

plot_spline((160.332, 50, 90), (160.332, 32, 90), "thirdSeventh", 40, -8, -8, -4, False, 45, 30)