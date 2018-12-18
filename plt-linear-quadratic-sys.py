from matplotlib.widgets import Slider, Button, RadioButtons, TextBox
import matplotlib.pyplot as plt
import numpy as np


class Color:
    red = "red"
    green = "green"
    blue = "blue"
    lightgoldenrodyellow = "lightgoldenrodyellow"


factor = dict()
x = None


def init_equations_factors():
    # ax*2 + bx + c = 0
    factor["a"] = 1
    factor["b"] = 1
    factor["c"] = 1
    # dx + e = 0
    factor["d"] = 2
    factor["e"] = 2


def init_subplot():
    global x
    fig, ax = plt.subplots(figsize=FIG_SIZE)
    plt.subplots_adjust(left=0.25, bottom=0.5)
    plt.axis([-RANGE, RANGE, -RANGE, RANGE], )
    x = np.arange(-RANGE, RANGE, STEP)


def init_sliders():
    ax_a = plt.axes([left_offset, 0.05, right_offset, top_offset], facecolor=Color.lightgoldenrodyellow)
    Slider(ax_a, 'a', -RANGE, RANGE, valinit=factor["a"]).on_changed(update)
    ax_b = plt.axes([left_offset, 0.1, right_offset, top_offset], facecolor=Color.lightgoldenrodyellow)
    Slider(ax_b, 'b', -RANGE, RANGE, valinit=factor["b"]).on_changed(update)
    ax_c = plt.axes([left_offset, 0.15, right_offset, top_offset], facecolor=Color.lightgoldenrodyellow)
    Slider(ax_c, 'c', -RANGE, RANGE, valinit=factor["c"]).on_changed(update)
    ax_d = plt.axes([left_offset, 0.25, right_offset, top_offset], facecolor=Color.lightgoldenrodyellow)
    Slider(ax_d, 'd', -RANGE, RANGE, valinit=factor["d"]).on_changed(update)
    ax_e = plt.axes([left_offset, 0.3, right_offset, top_offset], facecolor=Color.lightgoldenrodyellow)
    Slider(ax_e, 'e', -RANGE, RANGE, valinit=factor["e"]).on_changed(update)


def init_equations_funcs():
    quadratic = (factor["a"] * x) ** 2 + factor["b"] * x + factor["c"]
    linear = factor["d"] * x + factor["e"]
    quad, = plt.plot(x, quadratic, lw=1, color=Color.green)
    line, = plt.plot(x, linear, lw=1, color=Color.blue)
    intersect, = plt.plot(0, 0, 'ro')


def update(val):
    pass


if __name__ == "__main__":
    STEP = 0.1
    RANGE = 20.0
    FIG_SIZE = (9, 5)
    left_offset = 0.25
    right_offset = 0.6
    top_offset = 0.03
    init_equations_factors()
    init_subplot()
    init_equations_funcs()
    init_sliders()
    plt.show()
