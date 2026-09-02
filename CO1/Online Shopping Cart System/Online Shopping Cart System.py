# Online Fruit Shopping Cart

cart = {}


def add_fruit(name, price, quantity):
    if name in cart:
        cart[name]["quantity"] += quantity
    else:
        cart[name] = {
            "price": price,
            "quantity": quantity
        }


def remove_fruit(name):
    if name in cart:
        del cart[name]


def change_quantity(name, quantity):
    if name in cart:
        cart[name]["quantity"] = quantity


def calculate_subtotal():
    subtotal = 0

    for fruit in cart.values():
        subtotal += fruit["price"] * fruit["quantity"]

    return subtotal


def calculate_gst(amount):
    return amount * 18 / 100


def apply_discount(amount):
    return amount * 10 / 100


def display_bill():
    subtotal = calculate_subtotal()
    discount = apply_discount(subtotal)
    amount_after_discount = subtotal - discount
    gst = calculate_gst(amount_after_discount)
    final_amount = amount_after_discount + gst

    print("\n========== FRUIT BILL ==========")

    for name, fruit in cart.items():
        total = fruit["price"] * fruit["quantity"]
        print(name, "x", fruit["quantity"], "=", total)

    print("-------------------------------")
    print("Subtotal :", subtotal)
    print("Discount (10%) :", discount)
    print("GST (18%) :", gst)
    print("Final Bill :", final_amount)
    print("===============================")


# Add fruits
add_fruit("Apple", 120, 2)
add_fruit("Banana", 60, 1)
add_fruit("Mango", 150, 3)

# Change quantity
change_quantity("Banana", 2)

# Remove a fruit
remove_fruit("Apple")

# Display final bill
display_bill()