1. Question Meaning

An enterprise application has different types of objects:

Customer
Product
Employee

All of them need similar operations, such as:

Add an object
Get an object
Display all objects

Instead of writing the same repository code three times, we can write one reusable repository using Generic Types.

2. Problem Identification

Without generics, we might create three separate classes:

CustomerRepository
ProductRepository
EmployeeRepository

But their logic is almost the same.

This causes:

Repeated code
More maintenance
Less reusability
Solution

Create one generic Repository class that can work with any object type.

3. Method Used: Generic Types

Python provides generics through the typing module.

We can use:

from typing import Generic, TypeVar

Then create a type variable:

T = TypeVar("T")

T represents any type.

Then:

class Repository(Generic[T]):

means:

This repository can work with any type of object.

For example:

Repository[Customer]
Repository[Product]
Repository[Employee]

All three use the same repository logic.

4. Simple Python Code
from typing import Generic, TypeVar

# T can represent any type
T = TypeVar("T")


class Repository(Generic[T]):

    def __init__(self):
        self.items: list[T] = []

    def add(self, item: T) -> None:
        self.items.append(item)

    def get_all(self) -> list[T]:
        return self.items


# Customer class
class Customer:
    def __init__(self, name: str):
        self.name = name


# Product class
class Product:
    def __init__(self, name: str):
        self.name = name


# Employee class
class Employee:
    def __init__(self, name: str):
        self.name = name


# Create repositories
customer_repo = Repository[Customer]()
product_repo = Repository[Product]()
employee_repo = Repository[Employee]()

# Add objects
customer_repo.add(Customer("Ravi"))
product_repo.add(Product("Laptop"))
employee_repo.add(Employee("Sita"))

# Display objects
print("Customer:", customer_repo.get_all()[0].name)
print("Product:", product_repo.get_all()[0].name)
print("Employee:", employee_repo.get_all()[0].name)
Output
Customer: Ravi
Product: Laptop
Employee: Sita
5. Understanding the Important Part
Type variable
T = TypeVar("T")

T is a placeholder for a type.

It can become:

T = Customer
T = Product
T = Employee
Generic Repository
class Repository(Generic[T]):

This means the repository can store any type of object.

Add method
def add(self, item: T) -> None:

The item must be the same type used by the repository.

For example:

customer_repo = Repository[Customer]()

So this repository is intended for Customer objects.

**6. Simple Real-Life Example**

Think of a storage box.

Instead of creating:

CustomerBox
ProductBox
EmployeeBox

we create one:

GenericBox

Then we can use it as:

GenericBox<Customer>
GenericBox<Product>
GenericBox<Employee>

The storage logic remains the same.

**7. Algorithm**

Start

Import Generic and TypeVar.

Create a type variable T.

Create a generic Repository class.

Create a list to store objects.

Create an add() method to add objects.

Create a get_all() method to retrieve objects.

Create Customer, Product, and Employee classes.

Create a repository for each type.

Add customer, product, and employee objects.

Display the stored objects.

Stop
8. Final Answer in Simple Words

The problem is that Customer, Product, and Employee need the same repository operations, which can lead to repeated code. The solution is to use Generic Types. TypeVar creates a type placeholder, and Generic[T] allows one Repository class to work with different object types. Thus, Repository[Customer], Repository[Product], and Repository[Employee] can reuse the same repository logic.
