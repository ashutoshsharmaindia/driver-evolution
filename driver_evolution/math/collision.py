def limit(lower, upper, num):
    if num < lower:
        return lower
    elif num > upper:
        return upper
    return num


def calc_dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def slope_and_intercept(p1, p2):
    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    intercept = p1[1] - (p1[0] * slope)
    return slope, intercept


def circle_to_circle(c1, r1, c2, r2):
    center_dist = calc_dist(c1, c2)
    return center_dist <= r1 + r2


def circle_to_line(c, r, p1, p2):
    if p1[0] == p2[0]:  # vertical line
        y1, y2 = sorted([p1[1], p2[1]])  # get lower and higher y value
        limit_y = limit(y1, y2, c[1])
        return calc_dist(c, (p1[0], limit_y)) <= r
    elif p1[1] == p2[1]:  # horizontal
        x1, x2 = sorted([p1[0], p2[0]])  # get lower and higher x value
        limit_x = limit(x1, x2, c[0])
        return calc_dist(c, (limit_x, p1[1])) <= r
    else:  # non-straight line
        slope, intercept = slope_and_intercept(p1, p2)
        int_x = (-slope * intercept + slope * c[1] + c[0]) / (slope ** 2 + 1)
        x1, x2 = sorted([p1[0], p2[0]])  # get lower and higher x value
        int_x = limit(x1, x2, int_x)
        int_y = slope * int_x + intercept
        return calc_dist((int_x, int_y), c) <= r
