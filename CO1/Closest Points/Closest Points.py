import math

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def closest_pair(points):
    min_distance = float('inf')
    closest_points = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = distance(points[i], points[j])

            if d < min_distance:
                min_distance = d
                closest_points = (points[i], points[j])

    return closest_points, min_distance


# Example points
points = [
    (2, 3),
    (12, 30),
    (40, 50),
    (5, 1),
    (12, 10),
    (3, 4)
]

pair, min_distance = closest_pair(points)

print("Closest points:", pair)
print("Minimum distance:", min_distance)