# Merge Sort in descending order

def merge_sort(students):
    if len(students) <= 1:
        return students

    mid = len(students) // 2

    left = merge_sort(students[:mid])
    right = merge_sort(students[mid:])

    return merge(left, right)


def merge(left, right):
    result = []
    i = 0
    j = 0

    # Descending order
    while i < len(left) and j < len(right):
        if left[i][1] >= right[j][1]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Add remaining students
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Student names and marks
students = [
    ("Anita", 95),
    ("Vivek", 83),
    ("Lakshmi", 66),
    ("Ramesh", 97),
    ("Kumar", 85)
]

# Sort students using Merge Sort
students = merge_sort(students)

print("Students in descending order:")
for name, marks in students:
    print(name, marks)

# Scholarship eligibility
print("\nStudents eligible for scholarship:")
for name, marks in students:
    if marks >= 90:
        print(name, marks)
```

**Output:**

```text
Students in descending order:
Ramesh 97
Anita 95
Kumar 85
Vivek 83
Lakshmi 66

Students eligible for scholarship:
Ramesh 97
Anita 95
```
