from math import sin, cos, atan2, pi
from random import random


def add(a, b):
    return [sum(comp) for comp in zip(a, b)]


def mult(a, c):
    return [comp * c for comp in a]


def mag(a):
    return sum([comp ** 2 for comp in a]) ** 0.5


def ang(a):
    atan2(a[1], a[0])


def from_ang_mag(ang, mag):
    x = cos(ang) * mag
    y = sin(ang) * mag
    return x, y


rand_vec = lambda: from_ang_mag(random() * 2 * pi, 1)
sub = lambda a, b: add(a, mult(b, -1))
div = lambda a, c: mult(a, 1 / c)
normalize = lambda a: div(a, mag(a))
set_mag = lambda a, m: mult(normalize(a), m)


def limit_mag(a, limit):
    if mag(a) > limit:
        return mult(normalize(a), limit)
    return a
