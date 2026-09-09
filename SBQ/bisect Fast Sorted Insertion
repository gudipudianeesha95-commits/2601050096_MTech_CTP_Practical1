## `bisect` – Fast Sorted Insertion

Python's **`bisect` module** is used to insert elements into a **sorted list** while keeping the list sorted.

### Simple Example

```python
import bisect

prices = [100, 250, 500, 1000]

bisect.insort(prices, 750)

print(prices)
```

### Output

```text
[100, 250, 500, 750, 1000]
```

### How it works

Initially:

```text
100   250   500   1000
```

We want to insert:

```text
750
```

`bisect.insort()` automatically finds the correct position:

```text
100   250   500   750   1000
```

So we **don't need to manually search** for where `750` should be inserted.

### Important Functions

| Function          | Purpose                                             |
| ----------------- | --------------------------------------------------- |
| `bisect.bisect()` | Finds the position where an item should be inserted |
| `bisect.insort()` | Inserts the item while maintaining sorted order     |

Example:

```python
import bisect

prices = [100, 250, 500, 1000]

position = bisect.bisect(prices, 750)
print("Position:", position)

bisect.insort(prices, 750)
print("Prices:", prices)
```

Output:

```text
Position: 3
Prices: [100, 250, 500, 750, 1000]
```

### Exam Definition

**`bisect` is a Python module that provides efficient methods for finding insertion positions and inserting elements into sorted lists while maintaining their sorted order.**

**Key idea:**
`bisect` → **Sorted list + Fast insertion**.
