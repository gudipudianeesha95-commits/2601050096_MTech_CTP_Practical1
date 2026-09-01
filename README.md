**Binary Search Book System**

**1. Objective**

To develop a Python-based book searching system that uses the Binary Search algorithm to find a specific book number from a sorted list of books and display its position.

**2. Input**

The program accepts:

    Sorted list of book numbers from 1 to 10 lakh
    Target book number to be searched

In this program, the target book number is 75000.

**3. Output**

The program displays:

    Whether the book exists
    Book number
    Location or position of the book
    Appropriate message if the book does not exist

**4. Algorithm**

    Start.
    Create a sorted list of books numbered from 1 to 10 lakh.
    Set the target book number to 75000.
    Set the lower limit to the first position of the list.
    Set the upper limit to the last position of the list.
    Find the middle position between the lower and upper limits.
    Compare the book number at the middle position with the target book number.
    If the middle book number is equal to the target, the book is found.
    If the middle book number is smaller than the target, search in the right half of the list.
    If the middle book number is greater than the target, search in the left half of the list.
    Continue the search until the book is found or the lower limit becomes greater than the upper limit.
    If the book is found, display that the book exists along with its number and position.
    If the book is not found, display that the book does not exist.
    Stop.

**5. Time Complexity**

Let n be the number of books.

    Binary Search: O(log n)
    Comparison: O(1)
    Finding the middle position: O(1)
    Updating the search limits: O(1)

Therefore, the overall time complexity of the Binary Search operation is O(log n).

**6. Space Complexity**

O(n)

The program stores the list of n book numbers in memory. The Binary Search operation itself uses O(1) extra space.
