def add(a, b):
    return [sum(comp) for comp in zip(a, b)]


def mult(a, c):
    return [comp * c for comp in a]


def mag(a):
    return sum([comp ** 2 for comp in a]) ** 0.5


sub = lambda a, b: add(a, mult(b, -1))
div = lambda a, c: mult(a, 1 / c)
normalize = lambda a: div(a, mag(a))
set_mag = lambda a, m: mult(normalize(a), m)


def limit_mag(a, limit):
    if mag(a) > limit:
        return mult(normalize(a), limit)
    return a
