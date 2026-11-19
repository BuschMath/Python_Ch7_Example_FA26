import math
#points are equal-length lists or tuples
def euclidD(point1, point2):
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total += diff

    euclidDistance = math.sqrt(total)
    return euclidDistance

pt1 = (0, 0, 0, 0)
pt2 = (3, 4, 5, 6)
distance = euclidD(pt1, pt2)
print("The Euclidean distance between", pt1, "and", pt2, "is:", distance)