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

Start. 
Create a list containing the given two-dimensional points. 
Set the minimum distance to infinity. 
Set the closest pair of points as empty. Select the first point from the list. 
Select the next point from the list. 
Calculate the Euclidean distance between the two selected points using the difference between their x-coordinates and y-coordinates. 
Compare the calculated distance with the current minimum distance. 
If the calculated distance is smaller, update the minimum distance. Store the two selected points as the closest pair. 
Continue comparing the first point with all the points that come after it. 
Repeat the same process for every point in the list. 
After all pairs of points have been compared, return the closest pair and the minimum distance. 
Display the closest points. Display the minimum distance. Stop.

**5. Time Complexity**

Let n be the number of points.

Calculate distance: O(1) Compare all pairs of points: O(n²) Find minimum distance: O(1) for each comparison

Therefore, the overall time complexity is O(n²).

**6. Space Complexity**

O(1)

The algorithm uses only a constant amount of extra space for storing the minimum distance, closest pair, and temporary distance. The input list of points itself requires O(n) space.
