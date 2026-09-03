**Online Fruit Shopping Cart**

**1. Objective**

To develop a Python-based online fruit shopping cart system that allows fruits to be added to the cart, quantities to be changed, fruits to be removed, and the final bill to be calculated after applying a discount and GST.

**2. Input**

The program accepts:

Fruit name Price of each fruit Quantity of each fruit Updated quantity of a fruit

The program uses the following fruits:

Apple – ₹120 Banana – ₹60 Mango – ₹150

The Banana quantity is changed to 2, and Apple is removed from the cart.

**3. Output**

The program displays:

Fruit name Quantity of each fruit Price for each fruit Subtotal 10% discount 18% GST Final bill amount

For the given input:

Banana = ₹120 Mango = ₹450 Subtotal = ₹570 Discount = ₹57 GST = ₹92.34 Final Bill = ₹605.34

**4. Algorithm**

1.Start. 
2.Create an empty shopping cart to store fruit details. 
3.Add Apple to the cart with its price and quantity. 
4.Add Banana to the cart with its price and quantity. 
5.Add Mango to the cart with its price and quantity. 
6.Check whether a fruit already exists in the cart when adding it. 
7.If the fruit already exists, increase its quantity. Otherwise, add the fruit with its price and quantity. 
8.Change the quantity of Banana to 2. 
9.Remove Apple from the cart. 
10.Calculate the subtotal by multiplying the price of each fruit by its quantity and adding all the amounts. 
11.Calculate a 10% discount on the subtotal. 
12.Subtract the discount from the subtotal to calculate the amount after discount. 
13.Calculate 18% GST on the amount after discount. 
14.Add the GST to the amount after discount to calculate the final bill. 
15.Display each fruit, its quantity, and its total price. 
16.Display the subtotal, discount, GST, and final bill. 
17.Stop.

**5. Time Complexity**

Let n be the number of fruits in the shopping cart.

Add Fruit: O(1) on average Remove Fruit: O(1) on average Change Quantity: O(1) on average Calculate Subtotal: O(n) Calculate GST: O(1) Apply Discount: O(1) Display Bill: O(n)

Therefore, the overall time complexity for calculating and displaying the bill is O(n).

**6. Space Complexity**

O(n)

The shopping cart dictionary stores the name, price, and quantity of each fruit in the cart.

