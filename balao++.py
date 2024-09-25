from math import floor
r, l = [int(x) for x in input().split()]
pi = 3.1415
print(floor(l/((4 * pi * r ** 3)/3)))