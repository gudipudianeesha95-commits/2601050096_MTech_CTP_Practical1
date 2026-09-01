**Maximum Subarray – Daily Profit System**

**1. Objective**

To develop a Python-based system that finds the maximum profit that can be earned over a sequence of consecutive days using the Maximum Subarray algorithm.

**2. Input**

The program accepts:

A list of daily profits and losses

In this program, the daily profits and losses are:

100
-50
200
-100
300
-50
150

**3. Output**

The program displays:

Daily profits and losses
Maximum profit obtained from consecutive days

For the given input, the maximum profit is 550.

**4. Algorithm**

Start.
Create a list containing the daily profits and losses of the shop.
Set the current maximum profit to the profit of the first day.
Set the overall maximum profit to the profit of the first day.
Start checking the profits from the second day.
For each day, calculate the maximum profit that can be obtained by either starting a new sequence from the current day or adding the current day's profit to the previous sequence.
Update the current maximum profit with the larger value.
Compare the current maximum profit with the overall maximum profit.
If the current maximum profit is greater, update the overall maximum profit.
Continue this process until all days have been checked.
Return the overall maximum profit.
Display the daily profits and losses.
Display the maximum profit obtained from consecutive days.
Stop.

**5. Time Complexity**

Let n be the number of days.

Checking each day's profit: O(n)
Calculating the current maximum: O(1) for each day
Updating the maximum profit: O(1) for each day

Therefore, the overall time complexity is O(n).

**6. Space Complexity**

O(1)

The algorithm uses only a constant amount of extra space for storing the current maximum profit and overall maximum profit.
