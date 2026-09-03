**Product Price Sorting System**

**1. Objective**

To develop a Python-based product price sorting system that uses the Quick Sort algorithm to arrange products in ascending order based on their prices.

**2. Input**

The program accepts:

Product names Product prices

The given products are:

Laptop – ₹50,000 Mobile – ₹20,000 Headphones – ₹3,000 Tablet – ₹15,000 Keyboard – ₹2,000

**3. Output**

The program displays:

Products sorted according to their prices Product names Product prices

The products are arranged from lowest price to highest price.

**4. Algorithm**

1. Start.

2. Create a list containing product names and their prices.

3. Check whether the list contains zero or one product.

4. If the list contains zero or one product, return the list as it is.

5. Select the first product as the pivot.

6. Create two empty lists:

   * Left list for products with lower or equal prices.
   * Right list for products with higher prices.

7. Compare the price of each remaining product with the pivot price.

8. If the product price is less than or equal to the pivot price, place it in the left list.

9. If the product price is greater than the pivot price, place it in the right list.

10. Apply the same Quick Sort process recursively to the left list.

11. Apply the same Quick Sort process recursively to the right list.

12. Combine the sorted left list, pivot product, and sorted right list.

13. Return the completely sorted product list.

14. Display the products in ascending order of price.

15. Stop.


**5. Time Complexity**

Let n be the number of products.

Best/Average Case: O(n log n) Worst Case: O(n²) Comparing products: O(n) for each partition

Therefore, the average time complexity is O(n log n), while the worst-case time complexity is O(n²).

**6. Space Complexity**

O(n)

Additional lists are created to store products on the left and right of the pivot, and recursive calls also require additional memory.
