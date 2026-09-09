## Indian Banking System — OOP Concepts

This example demonstrates **Inheritance, Method Overriding, Abstract Base Class (ABC), Polymorphism, and the Liskov Substitution Principle**.

### 1. Basic Idea

A bank has different types of accounts:

```text
              BankAccount
                  |
          ┌───────┴───────┐
          ↓               ↓
   SavingsAccount    CurrentAccount
```

All accounts are **bank accounts**, but their operations can behave differently.

---

## 2. Simple Python Program

```python
from abc import ABC, abstractmethod

class BankAccount(ABC):

    @abstractmethod
    def withdraw(self, amount):
        pass


class SavingsAccount(BankAccount):

    def withdraw(self, amount):
        print("Withdrawal from savings account")


class CurrentAccount(BankAccount):

    def withdraw(self, amount):
        print("Withdrawal from current account")


accounts = [
    SavingsAccount(),
    CurrentAccount()
]

for account in accounts:
    account.withdraw(1000)
```

### Output

```text
Withdrawal from savings account
Withdrawal from current account
```

---

# 3. Explanation of Each Concept

### A. Inheritance

Inheritance means a child class gets properties or methods from a parent class.

```python
class SavingsAccount(BankAccount):
```

Here, `SavingsAccount` inherits from `BankAccount`.

Similarly:

```python
class CurrentAccount(BankAccount):
```

`CurrentAccount` also inherits from `BankAccount`.

---

### B. Abstract Base Class — ABC

```python
class BankAccount(ABC):
```

`BankAccount` is an **abstract class**.

It defines what an account **must do**, but does not provide the actual implementation.

```python
@abstractmethod
def withdraw(self, amount):
    pass
```

This says:

> Every type of bank account must provide a `withdraw()` method.

You cannot directly create:

```python
BankAccount()
```

because it contains an abstract method.

---

### C. Method Overriding

Both child classes provide their own implementation of `withdraw()`.

```python
class SavingsAccount(BankAccount):
    def withdraw(self, amount):
        print("Withdrawal from savings account")
```

and

```python
class CurrentAccount(BankAccount):
    def withdraw(self, amount):
        print("Withdrawal from current account")
```

The child class **overrides** the method defined by the parent class.

---

### D. Polymorphism

Polymorphism means **one interface, different behavior**.

Look at:

```python
for account in accounts:
    account.withdraw(1000)
```

The same statement:

```python
account.withdraw(1000)
```

produces different behavior depending on the account type.

For `SavingsAccount`:

```text
Withdrawal from savings account
```

For `CurrentAccount`:

```text
Withdrawal from current account
```

This is **polymorphism**.

---

### E. Liskov Substitution Principle (LSP)

The **Liskov Substitution Principle** says:

> A child class should be usable wherever its parent class is expected without breaking the program.

Here:

```python
accounts = [
    SavingsAccount(),
    CurrentAccount()
]
```

Both are treated as:

```text
BankAccount
```

and both can be used with:

```python
account.withdraw(1000)
```

So `SavingsAccount` and `CurrentAccount` can substitute for `BankAccount`.

---

## 4. Easy Real-Life Example

Think of `BankAccount` as a **common rule**:

```text
Every bank account must support withdrawal.
```

But the actual withdrawal process may differ:

```text
Savings Account → Apply savings-account rules
Current Account → Apply current-account rules
Salary Account  → Apply salary-account rules
```

The application can simply call:

```python
account.withdraw(1000)
```

without worrying about the exact account type.

---

## 5. Exam Summary

| Concept               | Meaning                                  | Example                        |
| --------------------- | ---------------------------------------- | ------------------------------ |
| **Inheritance**       | Child gets features from parent          | `SavingsAccount(BankAccount)`  |
| **ABC**               | Defines an abstract/common structure     | `class BankAccount(ABC)`       |
| **Abstract Method**   | Method that child classes must implement | `@abstractmethod`              |
| **Method Overriding** | Child provides its own implementation    | `withdraw()`                   |
| **Polymorphism**      | Same method, different behavior          | `account.withdraw()`           |
| **LSP**               | Child can replace parent safely          | Savings/Current as BankAccount |

### One-line exam answer

**The Indian Banking System example uses inheritance to create different account types, ABC to define common operations, method overriding to provide account-specific behavior, polymorphism to call the same method on different accounts, and LSP to ensure child accounts can be used wherever a `BankAccount` is expected.**
