def center_point(a, b, c, d):
    import math
    closer_x = 0
    closer_y = 0
    first_point_distance = math.sqrt(a**2 + b**2)
    second_point_distance = math.sqrt(c**2 + d**2)
    if first_point_distance > second_point_distance:
        closer_x = math.floor(c)
        closer_y = math.floor(d)
    else:
        closer_x = math.floor(a)
        closer_y = math.floor(b)
    return f"({closer_x}, {closer_y})"


x = float(input())
y = float(input())
z = float(input())
j = float(input())
print(center_point(x, y, z, j))