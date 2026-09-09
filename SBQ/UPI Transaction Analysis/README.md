## UPI Transaction Analysis — Simple Explanation

This program analyzes UPI transactions using **sets, dictionaries, Counter, comprehensions, and loops**.

### 1. Given Transactions

Each transaction is stored as a **tuple**:

```python
("T101", 500, "Chennai")
```

Here:

* `T101` → Transaction ID
* `500` → Amount
* `Chennai` → City

---

## 2. Python Program

```python
from collections import Counter

transactions = [
    ("T101", 500, "Chennai"),
    ("T102", 1200, "Bangalore"),
    ("T103", 500, "Chennai"),
    ("T104", 2500, "Mumbai"),
    ("T105", 500, "Chennai")
]

# Find unique cities
cities = {t[2] for t in transactions}
print("Cities:", cities)

# Count transactions by city
city_count = Counter(t[2] for t in transactions)
print("Transactions by city:", city_count)

# Find transactions above ₹1000
high_value = [t for t in transactions if t[1] > 1000]
print("High value transactions:", high_value)

# Calculate total transaction value
total = sum(t[1] for t in transactions)
print("Total:", total)
```

### Output

```text
Cities: {'Chennai', 'Bangalore', 'Mumbai'}

Transactions by city:
Counter({'Chennai': 3, 'Bangalore': 1, 'Mumbai': 1})

High value transactions:
[('T102', 1200, 'Bangalore'), ('T104', 2500, 'Mumbai')]

Total: 5200
```

> The order in which cities appear in a `set` can vary.

---

## 3. Explanation of Concepts

### A. Tuple

```python
("T101", 500, "Chennai")
```

A **tuple** stores related information together.

Here one transaction contains:

```text
Transaction ID + Amount + City
```

---

### B. Set

```python
cities = {t[2] for t in transactions}
```

A **set** stores only unique values.

The cities are:

```text
Chennai
Bangalore
Mumbai
```

Although Chennai appears 3 times, the set stores it only once.

**Result:**

```text
{'Chennai', 'Bangalore', 'Mumbai'}
```

---

### C. Counter

```python
city_count = Counter(t[2] for t in transactions)
```

`Counter` counts how many times each city occurs.

Transactions:

```text
Chennai    → 3
Bangalore  → 1
Mumbai     → 1
```

So:

```text
Counter({'Chennai': 3, 'Bangalore': 1, 'Mumbai': 1})
```

---

### D. List Comprehension

```python
high_value = [t for t in transactions if t[1] > 1000]
```

This finds transactions where the amount is **greater than ₹1,000**.

The amounts are:

```text
500
1200  ← selected
500
2500  ← selected
500
```

Therefore:

```text
T102 → ₹1200
T104 → ₹2500
```

---

### E. `sum()`

```python
total = sum(t[1] for t in transactions)
```

It adds all transaction amounts:

```text
500 + 1200 + 500 + 2500 + 500
= 5200
```

Therefore:

```text
Total = ₹5200
```

---

## 4. Algorithm

1. Start.
2. Store UPI transactions in a list of tuples.
3. Use a **set comprehension** to find unique cities.
4. Use `Counter` to count transactions for each city.
5. Use **list comprehension** to find transactions above ₹1,000.
6. Use `sum()` to calculate the total transaction value.
7. Display the results.
8. Stop.

### Exam Definition

**UPI Transaction Analysis** is the process of analyzing transaction data to find unique cities, count transactions, filter high-value transactions, and calculate total transaction value using Python data structures and functions.

### Quick Revision

| Concept           | Purpose                      |
| ----------------- | ---------------------------- |
| **Tuple**         | Stores one transaction       |
| **Set**           | Finds unique cities          |
| **Counter**       | Counts transactions by city  |
| **Comprehension** | Filters/extracts data easily |
| **Loop**          | Processes transactions       |
| **sum()**         | Calculates total amount      |
