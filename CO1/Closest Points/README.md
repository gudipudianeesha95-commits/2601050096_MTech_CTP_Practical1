**Closest Pair of Points System**

**1. Objective**

To develop a Python-based system that finds the two closest points from a given set of two-dimensional points and calculates the minimum Euclidean distance between them.

**2. Input**

The program accepts:

A list of two-dimensional points Each point contains an x-coordinate and a y-coordinate

In this program, the given points are:

(2, 3) (12, 30) (40, 50) (5, 1) (12, 10) (3, 4)

**3. Output**

The program displays:

The pair of closest points The minimum distance between the closest points

For the given points, the closest pair is (2, 3) and (3, 4).

**4. Algorithm**

1. Start.

2. Create a list containing the given two-dimensional points.

3. Set the minimum distance to infinity.

4. Set the closest pair of points as empty.

5. Select the first point from the list.

6. Select the next point from the list.

7. Calculate the Euclidean distance between the two selected points using their x-coordinates and y-coordinates.

8. Compare the calculated distance with the current minimum distance.

9. If the calculated distance is smaller than the minimum distance, update the minimum distance.

10. Store the two selected points as the closest pair.

11. Continue comparing the first point with all the points that come after it.

12. Repeat the same process for every point in the list.

13. After all pairs of points have been compared, return the closest pair and the minimum distance.

14. Display the closest points.

15. Display the minimum distance.

16. Stop.


**5. Time Complexity**

Let n be the number of points.

Calculate distance: O(1) Compare all pairs of points: O(n²) Find minimum distance: O(1) for each comparison

Therefore, the overall time complexity is O(n²).

**6. Space Complexity**

O(1)

The algorithm uses only a constant amount of extra space for storing the minimum distance, closest pair, and temporary distance. The input list of points itself requires O(n) space.
