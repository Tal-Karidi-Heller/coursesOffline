from functools import partialmethod
from math import atan2, degrees, cos, sin, radians
import matplotlib.pyplot as plt

def integral_aproximation(func_values, a, b):
    mean_values = sum(func_values) / len(func_values)
    return (b - a) * mean_values

def arrange(start, stop, step):
    _list = []
    for i in range(start, int(stop * (1 / step) + 1), 1):
        _list.append(i / (1 / step))
    return _list

    
def cubic_spline_course(point0, point1, v0, v1, wanted_speed, half_DBM, L, FBack):
    x0, y0, a0, x1, y1, a1 = point0[0], point0[1], point0[2], point1[0], point1[1], point1[2]
    a, b, c, d = (-2 * x1) + (v0 * cos(radians(a0))) + (2 * x0) + (v1 * cos(radians(a1))), (3 * x1) - (2 * v0 * cos(radians(a0))) - (3 * x0) - (v1 * cos(radians(a1))), v0 * cos(radians(a0)), x0
    e, f, g, h = (-2 * y1) + (v0 * sin(radians(a0))) + (2 * y0) + (v1 * sin(radians(a1))), (3 * y1) - (2 * v0 * sin(radians(a0))) - (3 * y0) - (v1 * sin(radians(a1))), v0 * sin(radians(a0)), y0

    def x(s): return a * pow(s, 3) + b * pow(s, 2) + c * s + d
    def y(s): return e * pow(s, 3) + f * pow(s, 2) + g * s + h

    def x_tag(s): return (3 * a * pow(s, 2)) + (2 * b * s) + c
    def y_tag(s): return (3 * e * pow(s, 2)) + (2 * f * s) + g
    def y_tagaim(s): return (6 * e * s) + (2 * f)
    def x_tagaim(s): return (6 * a * s) + (2 * b)

    if FBack == True:
        def angle(s): return degrees(atan2(y_tag(s), x_tag(s)))
    else:
        def angle(s): return degrees(atan2(y_tag(s), x_tag(s))) - 180

    def x_tilda(s): return x(s) + cos(radians(angle(s))) * L
    def y_tilda(s): return y(s) + sin(radians(angle(s))) * L


    def length(s):
        return pow(x_tag(s) ** 2 + y_tag(s) ** 2, 0.5)

    c_t, c_x, c_y = 0, x_tilda(0), y_tilda(0)
    print(c_x, c_y)
    points = []

    for s in arrange(0, 1, 0.0001):
        n_x, n_y, s = x_tilda(s), y_tilda(s), s
        lenght_of_line = pow((n_x - c_x) ** 2 + (n_y - c_y) ** 2, 0.5)
        c_t += lenght_of_line / wanted_speed

        this_point = {'t': c_t, 'x': n_x, 'y': n_y}
        points.append(this_point)
#yo yo
        c_x, c_y = n_x, n_y
    
    def find_closest_point(points, _time):
        _min = abs(_time - points[0]['t']); chose_point = points[0]; index = 0
        for point in points[1:]:
            score = abs(_time - point['t'])
            if score < _min:
                _min, chose_point = score, point
            else:
                return (chose_point, index)
            index += 1
        
        return (chose_point, index)
    
    arrangedPoints = []
    step = 0.01
    for t in arrange(0, points[-1]['t'], step):
        nPoint, index = find_closest_point(points, t)
        nPoint1 = find_closest_point(points, t + step)[0]

        nPoint["x velocity"], nPoint["y velocity"] = (nPoint1['x'] - nPoint['x']) / (nPoint1['t'] - nPoint['t']), (nPoint1['y'] - nPoint['y']) / (nPoint1['t'] - nPoint['t'])
        nPoint["t"] = round(nPoint["t"], 2)

        arrangedPoints.append(nPoint)
        
    
    return {'points': arrangedPoints, 'length': length(1), 'time': arrangedPoints[-1]['t']}

def plot_spline(point0, point1, number, WS, V0, V1, L, FBack):
    # cubic_spline_course(point0, point1, v0, v1, wanted_speed, half_DBM, L)
    course = cubic_spline_course(point0, point1, V0, V1, WS, 5.15, L, FBack)
    points, length, lastTime = course['points'], course['length'], course['time']
    print('\nlast time', lastTime)

    xPoints, yPoints = [point['x'] for point in points], [point['y'] for point in points]

    with open("points.py", "a") as file:
        file.write(f"\npoints_spline{number} = " + str(points) + "\n" + f"lastTime{number} = " + str(lastTime))
 
    plt.figure("x and y"); plt.plot(xPoints, yPoints)

    plt.show()

with open("points.py", "w") as file: file.write("")

"""
plot_spline(point0, point1, number, WS, V0, V1, L, FBack)
"""