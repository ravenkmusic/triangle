def equilateral(sides):
    if is_triangle(sides):
        return sides[0] ==sides[1] == sides[2] and sides[0] != 0
    return False

def is_triangle(sides):
    a, b, c = sorted(sides)
    return a + b > c  

def isosceles(sides):
    if is_triangle(sides):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
    return False


def scalene(sides):
    if is_triangle(sides):
        return sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]
    return False