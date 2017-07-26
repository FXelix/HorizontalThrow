import matplotlib.pyplot as plt

# g = Acceleration of gravity m/s**2
# v = velocity
# h = start height
# d = distance
# t = start time

# h(t) = -0.5*g*t**2
# h(x) = s = v*t = v*(2*h/g)**(1/2)


def define_plot():
    plt.title("Horizontal Throw")
    plt.xlabel("Distance")
    plt.ylabel("Height")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.legend()


def plot_line(g, h, v):
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


def plot_multiple(g=9.81, h=100, v_max=10):
    for v in range(1, v_max):
        plot_line(g, h, v)


plot_multiple(v_max=20)
define_plot()
plt.show()
