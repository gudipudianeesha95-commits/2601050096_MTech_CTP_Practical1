**Student Marks Management System**

**1. Objective**

To develop a Python-based student marks management system that uses the Merge Sort algorithm to arrange students in descending order of marks and identify students who are eligible for a scholarship.

**2. Input**

The program accepts:

Student names
Marks obtained by each student

The given students are:

Anita – 95
Vivek – 83
Lakshmi – 66
Ramesh – 97
Kumar – 85

The scholarship eligibility requirement is 90 marks or above.

**3. Output**

The program displays:

Students arranged in descending order of marks
Students eligible for the scholarship
Name and marks of each eligible student

The sorted output is:

Ramesh – 97
Anita – 95
Kumar – 85
Vivek – 83
Lakshmi – 66

**4. Algorithm**

Start.
Create a list containing student names and their marks.
Divide the list into two halves.
Continue dividing each half until each part contains only one student.
Compare the marks of students from the divided lists.
Select the student with the higher marks first to arrange the students in descending order.
Add the selected student to the sorted list.
Continue comparing and adding students until one of the lists becomes empty.
Add all the remaining students to the sorted list.
Merge the sorted parts together.
Continue the merging process until the complete student list is sorted in descending order of marks.
Display all students with their marks in descending order.
Check the marks of each student.
If a student's marks are 90 or above, display the student as eligible for the scholarship.
If the marks are below 90, do not include the student in the scholarship list.
Stop.

**5. Time Complexity**

Let n be the number of students.

Dividing the list: O(log n)
Merging the lists: O(n)
Overall Merge Sort: O(n log n)
Checking scholarship eligibility: O(n)

Therefore, the overall time complexity is O(n log n).

**6. Space Complexity**

O(n)

The Merge Sort algorithm requires additional space to store the divided and merged lists. The student records are also stored in the input list.
