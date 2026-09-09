# Backtracking – Route Generation

**Backtracking** is an algorithmic technique used to find **all possible solutions** by trying one choice at a time. If a choice leads to an invalid solution, the algorithm **goes back and tries another choice**.

### 🚆 Example

Suppose a passenger wants to travel from **A to D**.

Possible routes are:

```text
A → B → D
A → C → D
A → B → C → D
```

The algorithm explores the routes one by one.

### 🔄 Basic Idea

```text
             Choose a route
                   ↓
                Explore
                   ↓
                Valid?
               /      \
             Yes       No
              ↓         ↓
          Continue   Backtrack
                        ↓
                 Try another route
```

## Step-by-step

Suppose we start at **A**.

### Choice 1: A → B

From B, try:

```text
A → B → D
```

This is valid, so we save the route.

### Choice 2: A → C

Try:

```text
A → C → D
```

This is also valid, so we save it.

### Another choice

We can also explore:

```text
A → B → C → D
```

If at any point there is **no valid next station**, we remove the last station and go back.

That removal is called **backtracking**.

---

# 🐍 Simple Python Program

```python
graph = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': []
}

def find_routes(current, destination, path):
    path.append(current)

    if current == destination:
        print(" → ".join(path))
    else:
        for next_station in graph[current]:
            if next_station not in path:
                find_routes(next_station, destination, path)

    # Backtrack
    path.pop()


print("All possible routes:")
find_routes('A', 'D', [])
```

### Output

```text
All possible routes:
A → B → C → D
A → B → D
A → C → D
```

The exact order can depend on how the graph's neighboring stations are listed.

---

## 🔙 Why `path.pop()`?

This is the most important part of backtracking:

```python
path.pop()
```

Suppose we have:

```text
A → B → D
```

After exploring D, we remove D:

```text
A → B
```

Then remove B:

```text
A
```

Now the algorithm can try another choice:

```text
A → C → D
```

So the pattern is:

**Choose → Explore → Check → Backtrack → Try another choice**

---

## 📌 Applications of Backtracking

Backtracking is commonly used for:

* 🚆 Route generation
* 💺 Seat arrangement
* 📅 Timetable combinations
* 🧩 Constraint satisfaction problems
* 👑 N-Queens problem
* 🔢 Sudoku
* 🔤 Permutations and combinations

### ⭐ Exam Definition

> **Backtracking is an algorithmic technique that builds a solution step by step, and whenever a choice leads to an invalid solution, it removes that choice and goes back to try another possibility.**

### Easy way to remember

**Greedy:** Choose the best option and move forward.

**Dynamic Programming:** Solve and store smaller problems.

**Backtracking:** Try a choice → if it fails → **go back and try another choice**.

Available next action: Create a downloadable DOCX file here in this chat containing the editable prose above
