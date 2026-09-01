def quick_sort(products):
    if len(products) <= 1:
        return products

    pivot = products[0]

    left = []
    right = []

    for product in products[1:]:
        if product[1] <= pivot[1]:
            left.append(product)
        else:
            right.append(product)

    return quick_sort(left) + [pivot] + quick_sort(right)


products = [
    ("Laptop", 50000),
    ("Mobile", 20000),
    ("Headphones", 3000),
    ("Tablet", 15000),
    ("Keyboard", 2000)
]

products = quick_sort(products)

print("Products sorted by price:")

for name, price in products:
    print(name, price)