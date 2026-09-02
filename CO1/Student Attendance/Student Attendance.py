# Student Attendance Analysis System

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i + 1}")

    name = input("Student Name: ")
    total_classes = int(input("Total Classes Conducted: "))
    attended_classes = int(input("Total Classes Attended: "))

    # Calculate attendance percentage
    attendance = (attended_classes / total_classes) * 100

    students.append({
        "name": name,
        "total": total_classes,
        "attended": attended_classes,
        "attendance": attendance
    })

# Display attendance details
print("\n========== ATTENDANCE REPORT ==========")

for student in students:
    print(f"Name: {student['name']}")
    print(f"Classes Conducted: {student['total']}")
    print(f"Classes Attended: {student['attended']}")
    print(f"Attendance: {student['attendance']:.2f}%")

    if student["attendance"] < 75:
        print("Status: Below 75%")
    else:
        print("Status: Eligible")

    print("---------------------------------------")

# Students below 75%
below_75 = [s for s in students if s["attendance"] < 75]

print("\n========== STUDENTS BELOW 75% ==========")

if below_75:
    for student in below_75:
        print(f"{student['name']} - {student['attendance']:.2f}%")
else:
    print("No students are below 75%.")

# Find highest attendance student
highest_student = max(students, key=lambda s: s["attendance"])

print("\n========== HIGHEST ATTENDANCE ==========")
print(f"Student: {highest_student['name']}")
print(f"Attendance: {highest_student['attendance']:.2f}%")

# Calculate overall attendance
total_conducted = sum(s["total"] for s in students)
total_attended = sum(s["attended"] for s in students)

overall_attendance = (total_attended / total_conducted) * 100

print("\n========== OVERALL ATTENDANCE ==========")
print(f"Total Classes Conducted: {total_conducted}")
print(f"Total Classes Attended: {total_attended}")
print(f"Overall Attendance: {overall_attendance:.2f}%")
