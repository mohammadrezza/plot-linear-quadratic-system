from matplotlib.widgets import Slider, Button, RadioButtons, TextBox
import matplotlib.pyplot as plt
import numpy as np


class Color:
    red = "red"
    green = "green"
    blue = "blue"
    lightgoldenrodyellow = "lightgoldenrodyellow"


def init_equations_factors():
    # ax*2 + bx + c = 0
    factors["a"] = 1
    factors["b"] = 1
    factors["c"] = 1
    # dx + e = 0
    factors["d"] = 2
    factors["e"] = 2


def init_subplot():
    global x, fig, ax
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    plt.subplots_adjust(left=0.25, bottom=0.5)
    plt.axis([-RANGE, RANGE, -RANGE, RANGE], )
    x = np.arange(-RANGE, RANGE, STEP)


def init_sliders():
    global s_a, s_b, s_c, s_d, s_e, text_box
    # region creating axes
    ax_a = plt.axes([left_offset, 0.05, right_offset, top_offset], facecolor=Color.lightgoldenrodyellow)
    ax_b = plt.axes([left_offset, 0.1, right_offset, top_offset], facecolor=Color.lightgoldenrodyellow)
    ax_c = plt.axes([left_offset, 0.15, right_offset, top_offset], facecolor=Color.lightgoldenrodyellow)
    ax_d = plt.axes([left_offset, 0.25, right_offset, top_offset], facecolor=Color.lightgoldenrodyellow)
    ax_e = plt.axes([left_offset, 0.3, right_offset, top_offset], facecolor=Color.lightgoldenrodyellow)
    ax_t = plt.axes([0.025, 0.5, 0.15, 0.15], facecolor=Color.lightgoldenrodyellow)
    # endregion creating axes
    # region creating sliders
    s_a = Slider(ax_a, 'a', -RANGE, RANGE, valinit=factors["a"])
    s_b = Slider(ax_b, 'b', -RANGE, RANGE, valinit=factors["b"])
    s_c = Slider(ax_c, 'c', -RANGE, RANGE, valinit=factors["c"])
    s_d = Slider(ax_d, 'd', -RANGE, RANGE, valinit=factors["d"])
    s_e = Slider(ax_e, 'e', -RANGE, RANGE, valinit=factors["e"])
    text_box = TextBox(ax_t, '')
    # endregion creating sliders
    # region set sliders listeners
    s_a.on_changed(update)
    s_b.on_changed(update)
    s_c.on_changed(update)
    s_d.on_changed(update)
    s_e.on_changed(update)
    # endregion set sliders listeners


def init_equations_funcs():
    global quad, line, intersect
    quadratic = (factors["a"] * x) ** 2 + factors["b"] * x + factors["c"]
    linear = factors["d"] * x + factors["e"]
    quad, = plt.plot(x, quadratic, lw=1, color=Color.green)
    line, = plt.plot(x, linear, lw=1, color=Color.blue)
    intersect, = plt.plot(0, 0, 'ro')


def update(val):
    global x
    a = s_a.val
    b = s_b.val
    c = s_c.val
    d = s_d.val
    e = s_e.val
    ys = []
    gs = []
    # calculate new y for quad
    for i in x:
        y = a * (i ** 2) + b * i + c
        ys.append(y)
    quad.set_data(x, ys)
    # calculate new y for linear
    for i in x:
        g = d * i + e
        gs.append(g)
    line.set_data(x, gs)
    # find if there is intersect
    confluence(x, np.array(ys), np.array(gs))
    # update UI
    fig.canvas.draw_idle()


def confluence(x, a, b):
    indx = np.argwhere(np.diff(np.sign(a - b))).flatten()
    if not indx.size:
        text_box.set_val("None")
        return
    points = ""
    intersect.set_data(x[indx], a[indx])
    if len(x[indx]) > 0 and len(a[indx]) > 0:
        if len(indx) == 1:
            points = str(round(float(x[indx][0]), 2)) + " , " + str(round(float(a[indx][0]), 2))
        else:
            points = str(round(float(x[indx][0]), 2)) + " , " + str(round(float(a[indx][0]), 2))
            points += "\n" + str(round(float(x[indx][1]), 2)) + " , " + str(round(float(a[indx][1]), 2))
        text_box.set_val(points)


if __name__ == "__main__":
    # region init variables
    x, fig, ax = None, None, None
    s_a, s_b, s_c, s_d, s_e, text_box = None, None, None, None, None, None
    quad, line, intersect = None, None, None
    STEP = 0.1
    RANGE = 20.0
    FIG_SIZE = (9, 5)
    left_offset = 0.25
    right_offset = 0.6
    top_offset = 0.03
    factors = dict()
    # endregion init variables
    # region init functions
    init_equations_factors()
    init_subplot()
    init_equations_funcs()
    init_sliders()
    # endregion init functions
    plt.show()
