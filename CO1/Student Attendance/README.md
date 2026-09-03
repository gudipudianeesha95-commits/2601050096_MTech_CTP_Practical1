**Student Attendance Analysis System**

**1. Objective**

To develop a Python-based student attendance analysis system that calculates individual attendance percentages, identifies students whose attendance is below 75%, finds the student with the highest attendance, and calculates the overall attendance percentage.

**2. Input**

The program accepts:

Number of students Student name Total classes conducted Total classes attended

The program calculates the attendance percentage for each student.

**3. Output**

The program displays:

Student name Total classes conducted Total classes attended Individual attendance percentage Attendance status List of students below 75% attendance Student with the highest attendance Highest attendance percentage Total classes conducted by all students Total classes attended by all students Overall attendance percentage

**4. Algorithm**

1. Start.

2. Create an empty list to store student attendance details.

3. Read the number of students.

4. For each student, read the student's name.

5. Read the total number of classes conducted.

6. Read the total number of classes attended.

7. Calculate the attendance percentage using:
   Attendance Percentage = (Attended Classes / Total Classes) × 100

8. Store the student's name, total classes, attended classes, and attendance percentage in the list.

9. Repeat steps 4 to 8 for all students.

10. Display the attendance details of each student.

11. Check the attendance percentage of each student.

12. If the attendance percentage is below 75%, display the status as "Below 75%".

13. Otherwise, display the status as "Eligible".

14. Create a list containing students whose attendance is below 75%.

15. Display the students who are below 75% attendance.

16. If no student is below 75%, display "No students are below 75%."

17. Find the student with the highest attendance percentage.

18. Display the name and attendance percentage of the student with the highest attendance.

19. Calculate the total number of classes conducted by all students.

20. Calculate the total number of classes attended by all students.

21. Calculate the overall attendance percentage using:
    Overall Attendance Percentage = (Total Attended Classes / Total Conducted Classes) × 100

22. Display the total classes conducted, total classes attended, and overall attendance percentage.

23. Stop.


**5. Time Complexity**

Let n be the number of students.

Reading student details: O(n) Displaying attendance details: O(n) Finding students below 75%: O(n) Finding highest attendance: O(n) Calculating overall attendance: O(n)

Therefore, the overall time complexity is O(n).

**6. Space Complexity**

O(n)

The program stores the attendance details of all students in a list. Therefore, the space required increases with the number of students.
