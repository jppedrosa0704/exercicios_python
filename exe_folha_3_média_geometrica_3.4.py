import math

def media_geom(xs):
    mult = 1
    for i in xs:
        mult *= i
    return f'{mult ** (1 / len(xs)):.2f}'


print(media_geom([5,8,9,6,4,1,3,4,7,10]))