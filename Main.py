import math
#points are equal-length lists or tuples
def euclidD(point1, point2):
    total = 0
    for index in range(len(point1)):
        diff = (point1[index] - point2[index]) ** 2
        total += diff

    euclidDistance = math.sqrt(total)
    return euclidDistance

def readFile(filename):
    with open(filename, "r") as dataFile:
        dataDict = {}

        key = 0
        for aLine in dataFile:
            key = key + 1
            score = int(aLine)

            dataDict[key] = [score]

    return dataDict

pt1 = (0, 0, 0, 0)
pt2 = (3, 4, 5, 6)
distance = euclidD(pt1, pt2)
print("The Euclidean distance between", pt1, "and", pt2, "is:", distance)

total = 0
aNum = 1
while aNum <= 10:
    total += aNum
    aNum += 2
print(total)