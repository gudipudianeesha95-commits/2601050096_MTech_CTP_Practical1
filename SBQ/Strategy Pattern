# UPI Payment System – Strategy Pattern

The **Strategy Pattern** is a design pattern used when we have **multiple ways of performing the same task** and we want to change the method at runtime.

In this example, the task is **making a payment**, but the payment method can be:

* UPI
* Credit Card
* Debit Card
* Net Banking

Instead of putting all these methods inside one large class, we create separate **strategy classes**.

---

## 1. Structure

```text
                 PaymentService
                       |
                    strategy
                       |
        ┌──────────────┼──────────────┐
        ↓              ↓              ↓
   UPIPayment     CardPayment    NetBankingPayment
```

Each class has a `pay()` method, but the implementation is different.

---

## 2. Simple Python Program

```python
class UPIPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class CardPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using Card")


class NetBankingPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using Net Banking")


class PaymentService:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


# Use UPI
payment = PaymentService(UPIPayment())
payment.make_payment(500)
```

### Output

```text
Paid ₹ 500 using UPI
```

---

# 3. Changing the Payment Method

The important feature is that we can **change the strategy at runtime**.

### Using Card

```python
payment = PaymentService(CardPayment())
payment.make_payment(1000)
```

Output:

```text
Paid ₹ 1000 using Card
```

### Using Net Banking

```python
payment = PaymentService(NetBankingPayment())
payment.make_payment(2000)
```

Output:

```text
Paid ₹ 2000 using Net Banking
```

The `PaymentService` class itself does **not need to be modified**.

---

## 4. Runtime Strategy Change

We can even change the strategy of the same object:

```python
class UPIPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using UPI")


class CardPayment:
    def pay(self, amount):
        print("Paid ₹", amount, "using Card")


class PaymentService:
    def __init__(self, strategy):
        self.strategy = strategy

    def make_payment(self, amount):
        self.strategy.pay(amount)


payment = PaymentService(UPIPayment())
payment.make_payment(500)

payment.strategy = CardPayment()
payment.make_payment(1000)
```

Output:

```text
Paid ₹ 500 using UPI
Paid ₹ 1000 using Card
```

Here, the strategy changed from **UPI → Card** while the program was running.

---

# 5. How Strategy Pattern Works

### Step 1

Create separate classes for different payment methods.

```text
UPIPayment
CardPayment
NetBankingPayment
```

### Step 2

Each class implements the same operation:

```python
pay(amount)
```

### Step 3

`PaymentService` receives a strategy:

```python
PaymentService(UPIPayment())
```

### Step 4

`PaymentService` calls:

```python
self.strategy.pay(amount)
```

The correct payment method is automatically used.

---

# 6. Why Use Strategy Pattern?

Without Strategy Pattern, we might write:

```python
if method == "UPI":
    ...
elif method == "Card":
    ...
elif method == "NetBanking":
    ...
```

As more payment methods are added, this class becomes large and difficult to maintain.

With Strategy Pattern:

```text
UPI          → UPIPayment
Credit Card  → CardPayment
Debit Card   → DebitCardPayment
Net Banking  → NetBankingPayment
```

Each payment algorithm is separated.

### Advantages

* Easy to add new payment methods
* Easy to change payment method at runtime
* Reduces large `if-else` statements
* Makes code easier to maintain
* Follows **separation of concerns**

---

## 7. Exam Definition

**Strategy Pattern is a behavioral design pattern that defines a family of algorithms, places each algorithm in a separate class, and allows the algorithm to be selected or changed at runtime without modifying the class that uses it.**

### One-line answer

> **The Strategy Pattern allows the payment algorithm to be changed at runtime without modifying `PaymentService`.**
