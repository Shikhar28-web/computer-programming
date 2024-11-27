# Create a Python program that uses tuples to represent points in a 2D space and calculate the distance between two points.


import math

def distance(point1, point2):
    return math.sqrt((point2[0] - point1[0]) ** 2 + (point2[1] - point1[1]) ** 2)

p1 = (1, 2)
p2 = (4, 6)
print(distance(p1, p2)) 
