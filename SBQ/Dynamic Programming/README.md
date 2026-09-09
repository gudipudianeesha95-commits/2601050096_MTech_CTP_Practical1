# Dynamic Programming – Indian Train Ticket Cost

Dynamic Programming (DP) is a technique used to solve problems by **breaking a big problem into smaller subproblems and storing their answers** so that we don't calculate the same thing again.

### 🚆 Example

Suppose a traveler wants to travel:

**Chennai → Bangalore → Hyderabad → Delhi**

Assume the ticket costs are:

| From → To             |  Cost |
| --------------------- | ----: |
| Chennai → Bangalore   |  ₹500 |
| Chennai → Hyderabad   |  ₹900 |
| Chennai → Delhi       | ₹2000 |
| Bangalore → Hyderabad |  ₹400 |
| Bangalore → Delhi     | ₹1200 |
| Hyderabad → Delhi     |  ₹600 |

We need to find the **minimum cost from Chennai to Delhi**.

### Step 1: Work backward

Minimum cost from **Hyderabad → Delhi**:

```text
₹600
```

Minimum cost from **Bangalore → Delhi**:

```text
Bangalore → Hyderabad → Delhi
= ₹400 + ₹600
= ₹1000
```

Compare with direct:

```text
Bangalore → Delhi = ₹1200
```

So:

```text
Minimum Bangalore → Delhi = ₹1000
```

Minimum cost from **Chennai → Delhi**:

```text
Chennai → Bangalore → Hyderabad → Delhi
= ₹500 + ₹400 + ₹600
= ₹1500
```

Compare:

```text
Chennai → Hyderabad → Delhi
= ₹900 + ₹600
= ₹1500
```

Direct:

```text
Chennai → Delhi = ₹2000
```

Therefore:

**Minimum cost = ₹1500**

---

## 💡 Why Dynamic Programming?

Suppose many routes use:

```text
Bangalore → Delhi
```

We don't calculate its minimum cost repeatedly.

We calculate it **once**:

```text
dp[Bangalore] = ₹1000
```

Then reuse it.

This is the main idea of DP.

### Two important concepts

**1. Overlapping Subproblems**

The same smaller problem can occur multiple times.

Example:

```text
Find minimum cost Bangalore → Delhi
```

may be needed from several different routes.

**2. Optimal Substructure**

The optimal solution to the complete problem contains optimal solutions to its smaller problems.

For example:

```text
Minimum Chennai → Delhi
=
Chennai → Bangalore cost
+
Minimum Bangalore → Delhi
```

---

# 1. Memoization

Memoization means **top-down DP**.

We use recursion and store already calculated results.

```python
cost = [
    [0, 500, 900, 2000],
    [0, 0, 400, 1200],
    [0, 0, 0, 600],
    [0, 0, 0, 0]
]

dp = [-1] * 4

def min_cost(city):
    if city == 3:
        return 0

    if dp[city] != -1:
        return dp[city]

    ans = float('inf')

    for next_city in range(city + 1, 4):
        ans = min(ans, cost[city][next_city] + min_cost(next_city))

    dp[city] = ans
    return ans


print("Minimum ticket cost:", min_cost(0))
```

### Output

```text
Minimum ticket cost: 1500
```

Here:

```text
dp[0] = 1500
dp[1] = 1000
dp[2] = 600
dp[3] = 0
```

---

# 2. Tabulation

Tabulation means **bottom-up DP**.

We start from the destination and calculate the answers backward.

```python
cost = [
    [0, 500, 900, 2000],
    [0, 0, 400, 1200],
    [0, 0, 0, 600],
    [0, 0, 0, 0]
]

dp = [0, 0, 0, 0]

# Delhi
dp[3] = 0

# Hyderabad
dp[2] = 600

# Bangalore
dp[1] = min(400 + dp[2], 1200 + dp[3])

# Chennai
dp[0] = min(
    500 + dp[1],
    900 + dp[2],
    2000 + dp[3]
)

print("Minimum ticket cost:", dp[0])
```

### Output

```text
Minimum ticket cost: 1500
```

### DP table

| City      | Minimum cost to Delhi |
| --------- | --------------------: |
| Chennai   |                 ₹1500 |
| Bangalore |                 ₹1000 |
| Hyderabad |                  ₹600 |
| Delhi     |                    ₹0 |

### ⭐ Simple definition for exams

> **Dynamic Programming is an algorithmic technique that solves a problem by dividing it into overlapping subproblems, storing their results, and reusing them to avoid repeated calculations.**

For the train problem:

```text
Chennai
   ↓ ₹500
Bangalore
   ↓ ₹400
Hyderabad
   ↓ ₹600
Delhi

Total = ₹1500
```

So, the **minimum ticket cost from Chennai to Delhi is ₹1500**.
