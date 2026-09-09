# 🛒 Indian E-Commerce Order Management Using Python

Suppose an Indian e-commerce company has **thousands of customer orders**. Each order contains information such as:

* Product ID
* Product name
* Price
* Quantity
* Customer details
* Order status

Python provides several data structures and concepts that make it easy to **store, search, process, and analyze orders efficiently**.

---

## 1. 📋 Sequences – List and Tuple

### List

A **list** stores multiple orders and can be modified.

```python
orders = [
    {"product": "Laptop", "price": 50000, "quantity": 1},
    {"product": "Mouse", "price": 1000, "quantity": 2},
    {"product": "Keyboard", "price": 2000, "quantity": 1}
]

print(orders)
```

A list is useful because the company can **add or remove orders**.

### Tuple

A tuple stores fixed information.

```python
product = ("P101", "Laptop", 50000)
print(product)
```

A tuple cannot normally be changed after creation.

---

# 2. 🗂️ Mapping – Dictionary

A **dictionary (`dict`)** stores information using **key-value pairs**.

```python
order = {
    "product": "Laptop",
    "price": 50000,
    "quantity": 1,
    "status": "Delivered"
}

print(order["product"])
print(order["price"])
```

### Output

```text
Laptop
50000
```

For e-commerce orders, dictionaries are very useful because each order has different fields.

---

# 3. 🔢 Sets

A **set** stores unique values.

For example, find unique products:

```python
products = {"Laptop", "Mouse", "Laptop", "Keyboard"}

print(products)
```

Output:

```text
{'Laptop', 'Mouse', 'Keyboard'}
```

The duplicate `"Laptop"` is automatically removed.

---

# 4. ✨ Comprehensions

Comprehensions provide a short way to create collections.

For example, get all product names:

```python
products = [order["product"] for order in orders]

print(products)
```

Output:

```text
['Laptop', 'Mouse', 'Keyboard']
```

### Calculate total order value

```python
total = sum(
    order["price"] * order["quantity"]
    for order in orders
)

print("Total:", total)
```

### Output

```text
Total: 54000
```

Calculation:

```text
Laptop   = 50000 × 1 = 50000
Mouse    = 1000 × 2 =  2000
Keyboard = 2000 × 1 =  2000
                     -----
                     54000
```

---

# 5. 🔄 Iterators

An **iterator** allows us to process items one at a time.

```python
orders = ["Laptop", "Mouse", "Keyboard"]

iterator = iter(orders)

print(next(iterator))
print(next(iterator))
print(next(iterator))
```

Output:

```text
Laptop
Mouse
Keyboard
```

This can be useful when processing a large number of orders **one by one**.

---

# 6. ⚡ Generators

A generator produces values **one at a time** instead of storing all results in memory.

```python
def order_products(orders):
    for order in orders:
        yield order["product"]

for product in order_products(orders):
    print(product)
```

Output:

```text
Laptop
Mouse
Keyboard
```

Generators are useful when dealing with **thousands or millions of orders** because they can process data incrementally.

---

# 7. 🔢 `collections.Counter`

`Counter` is useful for counting how many times each product occurs.

```python
from collections import Counter

products = [
    "Laptop",
    "Mouse",
    "Laptop",
    "Keyboard",
    "Mouse",
    "Laptop"
]

count = Counter(products)

print(count)
```

Output:

```text
Counter({'Laptop': 3, 'Mouse': 2, 'Keyboard': 1})
```

So:

```text
Laptop   → 3 orders
Mouse    → 2 orders
Keyboard → 1 order
```

---

# 8. 🦆 Duck Typing

**Duck typing** means Python cares about **what an object can do**, rather than what type it is.

Example:

```python
def display(item):
    print(item)

display("Laptop")
display(["Laptop", "Mouse"])
display(50000)
```

The function works with different types because it only needs the object to support the operation being performed.

Simple definition:

> **If an object behaves like the required object, Python can use it, regardless of its exact type.**

---

# 9. 🛡️ EAFP

EAFP means:

> **Easier to Ask for Forgiveness than Permission.**

Instead of checking whether a dictionary key exists first, we try to access it and handle the error.

```python
order = {
    "product": "Laptop",
    "price": 50000
}

try:
    print(order["status"])
except KeyError:
    print("Order status not available")
```

### Output

```text
Order status not available
```

This is a common Python programming style.

---

# 🧑‍💻 Complete Simple Example

```python
from collections import Counter

orders = [
    {"product": "Laptop", "price": 50000, "quantity": 1},
    {"product": "Mouse", "price": 1000, "quantity": 2},
    {"product": "Keyboard", "price": 2000, "quantity": 1},
    {"product": "Mouse", "price": 1000, "quantity": 1}
]

# Calculate total value
total = sum(
    order["price"] * order["quantity"]
    for order in orders
)

# Get product names
products = [order["product"] for order in orders]

# Count products
product_count = Counter(products)

# Unique products
unique_products = set(products)

print("Total:", total)
print("Product count:", product_count)
print("Unique products:", unique_products)
```

### Output

```text
Total: 55000
Product count: Counter({'Mouse': 2, 'Laptop': 1, 'Keyboard': 1})
Unique products: {'Laptop', 'Mouse', 'Keyboard'}
```

---

## ⭐ Quick Exam Summary

| Python Concept    | E-Commerce Use                                     |
| ----------------- | -------------------------------------------------- |
| **List**          | Store multiple orders                              |
| **Tuple**         | Store fixed product information                    |
| **Dictionary**    | Store details of each order                        |
| **Set**           | Find unique products                               |
| **Comprehension** | Quickly process orders                             |
| **Iterator**      | Process orders one at a time                       |
| **Generator**     | Efficiently process large order data               |
| **Counter**       | Count product/order occurrences                    |
| **Duck Typing**   | Work with objects based on behavior                |
| **EAFP**          | Handle missing/invalid order data using exceptions |

### 🎯 Main idea

```text
E-Commerce Orders
       ↓
   Python Data
   Structures
       ↓
List → Dict → Set → Tuple
       ↓
Comprehensions
       ↓
Iterators / Generators
       ↓
Counter + Duck Typing + EAFP
       ↓
Efficient Order Processing
```

**Expected result for your original example: `Total: 54000`**.
