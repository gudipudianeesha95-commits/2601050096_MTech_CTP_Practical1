# Indian Food Delivery – Factory Pattern

The **Factory Pattern** is a design pattern used to **create objects without directly writing the object-creation logic everywhere in the program**.

In this example, a food-delivery application has different delivery methods:

* 🚲 Bike Delivery
* 🚗 Car Delivery
* ⚡ Express Delivery

The user selects the delivery type, and the **Factory creates the correct object**.

---

## 1. Structure

```text
              DeliveryFactory
                    |
              create_delivery()
                    |
        ┌───────────┼────────────┐
        ↓           ↓            ↓
 BikeDelivery  CarDelivery  ExpressDelivery
```

---

## 2. Simple Python Program

```python id="fct82a"
class BikeDelivery:
    def deliver(self):
        print("Delivery by bike")


class CarDelivery:
    def deliver(self):
        print("Delivery by car")


class ExpressDelivery:
    def deliver(self):
        print("Express delivery")


class DeliveryFactory:

    @staticmethod
    def create_delivery(delivery_type):

        if delivery_type == "bike":
            return BikeDelivery()

        elif delivery_type == "car":
            return CarDelivery()

        elif delivery_type == "express":
            return ExpressDelivery()

        else:
            raise ValueError("Invalid delivery type")


# User selects bike
delivery = DeliveryFactory.create_delivery("bike")

delivery.deliver()
```

### Output

```text
Delivery by bike
```

---

# 3. How It Works

### Step 1: Create delivery classes

```python id="d5td8j"
class BikeDelivery:
    def deliver(self):
        print("Delivery by bike")
```

This class handles bike delivery.

Similarly:

```python id="y5c2zh"
class CarDelivery:
```

handles car delivery.

---

### Step 2: Create the Factory

```python id="1s5y3m"
class DeliveryFactory:
```

The factory is responsible for **creating the correct delivery object**.

---

### Step 3: `create_delivery()`

```python id="h4q12x"
@staticmethod
def create_delivery(delivery_type):
```

This method receives the user's choice.

For example:

```python id="z7t6jj"
DeliveryFactory.create_delivery("bike")
```

The factory checks:

```python id="a5j3qv"
if delivery_type == "bike":
    return BikeDelivery()
```

So it creates a `BikeDelivery` object.

---

### Step 4: Call `deliver()`

The returned object is stored in:

```python id="z5n8vy"
delivery
```

Then:

```python id="5d0n5j"
delivery.deliver()
```

calls the appropriate delivery method.

Output:

```text id="m9j1k2"
Delivery by bike
```

---

# 4. Different User Choices

### Bike

```python id="2h8j7p"
delivery = DeliveryFactory.create_delivery("bike")
delivery.deliver()
```

Output:

```text
Delivery by bike
```

### Car

```python id="n3k9x1"
delivery = DeliveryFactory.create_delivery("car")
delivery.deliver()
```

Output:

```text
Delivery by car
```

### Express

```python id="q7m4vb"
delivery = DeliveryFactory.create_delivery("express")
delivery.deliver()
```

Output:

```text
Express delivery
```

---

# 5. Why Use Factory Pattern?

Without a Factory, the application might directly create objects everywhere:

```python
BikeDelivery()
CarDelivery()
ExpressDelivery()
```

With a Factory, object creation is centralized:

```python
DeliveryFactory.create_delivery("bike")
```

This makes the code:

* Easier to maintain
* Easier to extend
* More organized
* Less tightly coupled
* Easier to modify

For example, if a new **DroneDelivery** is added, we can add a new class and update the factory.

---

## 6. Real-Life Example

Suppose the customer selects:

```text
Delivery Type → Bike
```

The application sends `"bike"` to the factory:

```text
User
 ↓
"bike"
 ↓
DeliveryFactory
 ↓
BikeDelivery object
 ↓
deliver()
 ↓
Delivery by bike
```

The user doesn't need to know **how the `BikeDelivery` object is created**.

---

## 7. Exam Definition

> **Factory Pattern is a creational design pattern that separates object creation from business logic and creates the appropriate object based on the user's requirement.**

### One-line answer

**Factory Pattern separates object creation from business logic, allowing the application to create the appropriate delivery object without directly creating it everywhere.**

### Quick Revision

| Concept             | Meaning                        |
| ------------------- | ------------------------------ |
| **Factory**         | Creates objects                |
| **BikeDelivery**    | Handles bike delivery          |
| **CarDelivery**     | Handles car delivery           |
| **ExpressDelivery** | Handles express delivery       |
| `create_delivery()` | Decides which object to create |
| `deliver()`         | Performs the delivery          |
| `ValueError`        | Handles invalid delivery type  |
