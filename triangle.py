def equilateral(sides):
    if sides[0] == sides[1] and sides[1] == sides[2] and sides[0] == sides[2] and sides[0] != 0:
        return True
    else:
        return False

def is_triangle(sides):
    if sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return True
    else:
        return False
    

def isosceles(sides):
    if sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2] and sides[0] + sides[1] >= sides[2] and sides[1] + sides[2] >= sides[0] and sides[0] + sides[2] >= sides[1]:
        return True
    if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2]:
        return False
    else:
        return False



def scalene(sides):
    if sides[0] != sides[1] and sides[0] != sides[2] and sides[1] != sides[2] and is_triangle(sides):
        return True
    else:
        return False