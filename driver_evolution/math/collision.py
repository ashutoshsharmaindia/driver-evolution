def limit(lower, upper, num):
    if num < lower:
        return lower
    elif num > upper:
        return upper
    return num


def calc_dist(p1, p2):
    return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5


def circle_to_circle(p1, r1, p2, r2):
    center_dist = calc_dist(p1, p2)
    return center_dist <= r1 + r2


def slope_and_intercept(p1, p2):
    slope = (p2[1] - p1[1]) / (p2[0] - p1[0])
    intercept = p1[1] - (p1[0] * slope)
    return slope, intercept


def circle_to_line(c1, r1, l1, l2):
    if l1[0] == l2[0]:  # vertical line
        y1, y2 = sorted([l1[1], l2[1]])  # get lower and higher y value
        limit_y = limit(y1, y2, c1[1])
        return calc_dist(c1, (l1[0], limit_y)) <= r1
    elif l1[1] == l2[1]:  # horizontal
        x1, x2 = sorted([l1[0], l2[0]])  # get lower and higher x value
        limit_x = limit(x1, x2, c1[0])
        return calc_dist(c1, (limit_x, l1[1])) <= r1
    else:  # non-straight line
        slope, intercept = slope_and_intercept(l1, l2)
        int_x = (-slope * intercept + slope * c1[1] + c1[0]) / (slope ** 2 + 1)
        x1, x2 = sorted([l1[0], l2[0]])  # get lower and higher x value
        int_x = limit(x1, x2, int_x)
        int_y = slope * int_x + intercept
        return calc_dist((int_x, int_y), c1) <= r1
