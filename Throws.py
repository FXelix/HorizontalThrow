
# g = Acceleration of gravity m/s**2
# v = velocity
# h = start height
# d = distance
# t = start time

# h(t) = -0.5*g*t**2
# h(x) = s = v*t = v*(2*h/g)**(1/2)

import matplotlib.pyplot as plt
from math import cos, tan, radians


def define_plot():
    plt.title("Horizontal Throw")
    plt.xlabel("Distance")
    plt.ylabel("Height")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.legend()


def plot_inclined(v_ges, a, h, g):
    t = 0
    coordinates = {"s_x": [],
                   "s_y": []}

    while True:
        height = t*tan(radians(a)) - (g/(2*(v_ges**2)*cos(radians(a))**2))*t**2
        if height < 0:
            break
        coordinates["s_x"].append(t)
        coordinates["s_y"].append(height)
        t += 1/100

    plt.plot(coordinates["s_x"], coordinates["s_y"], label="v={}".format(str(v_ges) + "m/s"))


def plot_horizontal(v, h, g):
    t = 0
    coordinates = {"s_x": [],
                   "s_y": []}

    while True:
        height = h - 0.5 * g * t ** 2
        if height < 0:
            break
        d = v * t
        coordinates["s_x"].append(d)
        coordinates["s_y"].append(height)
        t += 1 / 100
    plt.plot(coordinates["s_x"], coordinates["s_y"], label="v={}".format(str(v) + "m/s"))


def plot_multiple(g=9.81, h=100, v_max=10, linear=True):
    if linear:
        for v in range(1, v_max):
            plot_horizontal(v, h, g)
    else:
        for a in range(10,80,5):
            plot_inclined(v_max, a, h, g)

plot_multiple(v_max=50, linear=False)
define_plot()
plt.show()
