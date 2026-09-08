from typing import TypeVar, Generic

T = TypeVar("T")

class Repository(Generic[T]):
    def __init__(self):
        self.items = []

    def add(self, item: T):
        self.items.append(item)

    def show(self):
        for item in self.items:
            print(item)


# Customer repository
customer_repo = Repository[str]()
customer_repo.add("Ravi")
customer_repo.add("Sita")

# Product repository
product_repo = Repository[str]()
product_repo.add("Laptop")
product_repo.add("Mobile")

# Employee repository
employee_repo = Repository[str]()
employee_repo.add("John")
employee_repo.add("Priya")

print("Customers:")
customer_repo.show()

print("Products:")
product_repo.show()

print("Employees:")
employee_repo.show()
