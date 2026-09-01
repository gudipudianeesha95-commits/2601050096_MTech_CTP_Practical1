**Student Attendance Analysis System**

**1. Objective**

To develop a Python-based student attendance analysis system that calculates individual attendance percentages, identifies students whose attendance is below 75%, finds the student with the highest attendance, and calculates the overall attendance percentage.

**2. Input**

The program accepts:

Number of students
Student name
Total classes conducted
Total classes attended

The program calculates the attendance percentage for each student.

**3. Output**

The program displays:

Student name
Total classes conducted
Total classes attended
Individual attendance percentage
Attendance status
List of students below 75% attendance
Student with the highest attendance
Highest attendance percentage
Total classes conducted by all students
Total classes attended by all students
Overall attendance percentage

**4. Algorithm**

Start.
Create an empty list to store student attendance details.
Read the number of students.
For each student, read the student's name.
Read the total number of classes conducted.
Read the total number of classes attended.
Calculate the student's attendance percentage using the attended classes and total classes conducted.
Store the student's name, total classes, attended classes, and attendance percentage.
Repeat the process for all students.
Display the attendance details of each student.
Check each student's attendance percentage.
If the attendance is below 75%, display the status as "Below 75%".
Otherwise, display the status as "Eligible".
Create a list containing students whose attendance is below 75%.
Display the students who are below 75% attendance.
If no student is below 75%, display "No students are below 75%."
Find the student with the highest attendance percentage.
Display the name and attendance percentage of the student with the highest attendance.
Calculate the total number of classes conducted by all students.
Calculate the total number of classes attended by all students.
Calculate the overall attendance percentage using the total attended classes and total conducted classes.
Display the total classes conducted, total classes attended, and overall attendance percentage.
Stop.

**5. Time Complexity**

Let n be the number of students.

Reading student details: O(n)
Displaying attendance details: O(n)
Finding students below 75%: O(n)
Finding highest attendance: O(n)
Calculating overall attendance: O(n)

Therefore, the overall time complexity is O(n).

**6. Space Complexity**

O(n)

The program stores the attendance details of all students in a list. Therefore, the space required increases with the number of students.
