def longer_line(x1, y1, x2, y2, x3, y3, x4, y4):
    import math
    first_pair_line = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    second_pair_line = math.sqrt((x4 - x3)**2 + (y4 - y3)**2)
    if first_pair_line >= second_pair_line:
        first_point_distance = math.sqrt(x1**2 + y1**2)
        second_point_distance = math.sqrt(x2**2 + y2**2)
        x1 = math.floor(int(x1))
        y1 = math.floor(int(y1))
        x2 = math.floor(int(x2))
        y2 = math.floor(int(y2))
        if first_point_distance < second_point_distance:
            return f"({x1}, {y1})({x2}, {y2})"
        else:
            return f"({x2}, {y2})({x1}, {y1})"
    else:
        third_point_distance = math.sqrt((x3**2 + y3**2))
        fourth_point_distance = math.sqrt((x4**2 + y4**2))
        x3 = math.floor(int(x3))
        y3 = math.floor(int(y3))
        x4 = math.floor(int(x4))
        y4 = math.floor(int(y4))
        if third_point_distance < fourth_point_distance:
            return f"({x3}, {y3})({x4}, {y4})"
        else:
            return f"({x4}, {y4})({x3}, {y3})"


a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
g = float(input())
h = float(input())
print(longer_line(a, b, c, d, e, f, g, h))