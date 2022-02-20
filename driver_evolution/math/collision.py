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
        dist = abs(l1[0] - c1[0])
        return dist <= r1
    elif l1[1] == l2[1]:  # horizontal
        dist = abs(l1[1] - c1[1])
        return dist <= r1
    else:  # non-straight line
        slope, intercept = slope_and_intercept(l1, l2)
        int_x = (-slope * intercept + slope * c1[1] + c1[0]) / (slope ** 2 + 1)
        int_x = max(min(int_x, l2[0]), l1[0])  # limit to l1[0] <= int_x <= l2[0], finite line
        int_y = slope * int_x + intercept
        return calc_dist((int_x, int_y), c1) <= r1
