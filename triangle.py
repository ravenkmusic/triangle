def equilateral(sides):
    if sides[0] == sides[1] and sides[1] == sides[2] and sides[0] == sides[2] and sides[0] != 0:
        return True
    else:
        return False