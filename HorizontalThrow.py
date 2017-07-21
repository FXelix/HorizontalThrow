import matplotlib.pyplot as plt

# g = Acceleration of gravity m/s**2
# v = velocity
# h = startheight
# d = startdistance
# t = starttime

# h(t) = -0.5*g*t**2
# h(x) = s = v*t = v*(2*h/g)**(1/2)


def horizontal_throw(g=9.81, h=100, v=10, more_lines=False):
    
    if more_lines:
        for velocity in range(1, v+1):
            t = 0
            coordinates = {"s_x": [],
                          "s_y": []}

            while True:
                height = h-0.5*g*t**2
                if height < 0:
                    break
                d = velocity*t
                coordinates["s_x"].append(d)
                coordinates["s_y"].append(height)
                t += 1/1000
            plt.plot(coordinates["s_x"], coordinates["s_y"], label="v={}".format(str(velocity)+"m/s"))

    else:
        t = 0
        coordinates = {"s_x": [],
                       "s_y": []}
        while True:
                           
            height = h-0.5*g*t**2
            if height < 0:
                break
            d = v*t
            coordinates["s_x"].append(d)
            coordinates["s_y"].append(height)
            t += 1/100
        plt.plot(coordinates["s_x"], coordinates["s_y"], label="v={}".format(v))

    plt.title("Horizontal Throw")
    plt.xlabel("Distance")
    plt.ylabel("Height")
    plt.xlim(0,)
    plt.ylim(0,)
    plt.legend()

    plt.show()

horizontal_throw(more_lines=True)
