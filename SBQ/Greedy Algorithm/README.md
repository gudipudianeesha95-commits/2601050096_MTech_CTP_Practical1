# Greedy Algorithm – Job Scheduling

A **Greedy Algorithm** solves a problem by making the **best possible choice at each step**, hoping that these choices lead to the overall best solution.

## 💼 Problem

A software company has the following jobs:

| Job | Start | Finish |
| --- | ----: | -----: |
| A   |     9 |     10 |
| B   |     9 |     12 |
| C   |    10 |     11 |
| D   |    11 |     13 |
| E   |    12 |     14 |

One employee can work on **only one job at a time**.

### 🎯 Goal

Select the **maximum number of non-overlapping jobs**.

---

## 🧠 Greedy Strategy

The strategy is:

> **Always choose the job that finishes earliest.**

Why?

Choosing a job that finishes early leaves **more time for the remaining jobs**.

---

## Step-by-Step

### Step 1: Sort jobs by finish time

They are already sorted:

```text
A → C → B → D → E
```

### Step 2: Select Job A

```text
A: 9 → 10
```

A is selected because it finishes earliest.

### Step 3: Find the next compatible job

The next job must start at **10 or later**.

Job C:

```text
C: 10 → 11
```

Select C.

### Step 4: Find the next compatible job

The next job must start at **11 or later**.

Job D:

```text
D: 11 → 13
```

Select D.

### Step 5: Check remaining jobs

Job E:

```text
E: 12 → 14
```

It starts at 12, but D finishes at 13.

Therefore, E overlaps with D and cannot be selected.

---

## ✅ Final Selection

```text
A → C → D
```

Number of jobs:

```text
3
```

So, the **maximum number of non-overlapping jobs is 3**.

---

# 🐍 Simple Python Program

```python
jobs = [
    ("A", 9, 10),
    ("B", 9, 12),
    ("C", 10, 11),
    ("D", 11, 13),
    ("E", 12, 14)
]

# Sort jobs according to finish time
jobs.sort(key=lambda x: x[2])

selected = []
last_finish = 0

for job in jobs:
    name, start, finish = job

    if start >= last_finish:
        selected.append(name)
        last_finish = finish

print("Selected jobs:", selected)
print("Maximum number of jobs:", len(selected))
```

### Output

```text
Selected jobs: ['A', 'C', 'D']
Maximum number of jobs: 3
```

---

## 🔑 Algorithm

1. Start.
2. Store all jobs with their start and finish times.
3. Sort the jobs according to **finish time**.
4. Select the first job.
5. Store its finish time.
6. Check the remaining jobs.
7. If a job's start time is greater than or equal to the previous job's finish time, select it.
8. Repeat until all jobs are checked.
9. Print the selected jobs.
10. Stop.

---

## 📌 Applications

The same greedy idea is useful in:

* 👨‍💼 Employee/job scheduling
* 📅 Meeting scheduling
* 🏫 Classroom scheduling
* 💻 CPU scheduling
* 📆 Activity selection problems

### ⭐ Exam Definition

> **Greedy algorithm is an algorithmic technique that makes the locally optimal choice at each step with the aim of obtaining a globally optimal solution.**

For this problem:

**Greedy choice = Select the job that finishes earliest.**

**Answer = A → C → D = 3 jobs.**

I can also show you the **difference between Greedy Algorithm and Dynamic Programming** using these two examples side by side.
