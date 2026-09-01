**Product Price Sorting System**

**1. Objective**

To develop a Python-based product price sorting system that uses the Quick Sort algorithm to arrange products in ascending order based on their prices.

**2. Input**

The program accepts:

Product names
Product prices

The given products are:

Laptop – ₹50,000
Mobile – ₹20,000
Headphones – ₹3,000
Tablet – ₹15,000
Keyboard – ₹2,000

**3. Output**

The program displays:

Products sorted according to their prices
Product names
Product prices

The products are arranged from lowest price to highest price.

**4. Algorithm**

Start.
Create a list containing product names and their prices.
Check whether the list contains zero or one product.
If the list contains zero or one product, return the list as it is.
Select the first product as the pivot.
Create two empty lists for products with lower or equal prices and products with higher prices.
Compare the price of each remaining product with the pivot price.
If a product's price is less than or equal to the pivot price, place it in the left list.
If a product's price is greater than the pivot price, place it in the right list.
Apply the same Quick Sort process recursively to the left list.
Apply the same Quick Sort process recursively to the right list.
Combine the sorted left list, pivot product, and sorted right list.
Return the completely sorted product list.
Display the products in ascending order of price.
Stop.

**5. Time Complexity**

Let n be the number of products.

Best/Average Case: O(n log n)
Worst Case: O(n²)
Comparing products: O(n) for each partition

Therefore, the average time complexity is O(n log n), while the worst-case time complexity is O(n²).

**6. Space Complexity**

O(n)

Additional lists are created to store products on the left and right of the pivot, and recursive calls also require additional memory.
