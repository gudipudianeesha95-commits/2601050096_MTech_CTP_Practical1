**Car Parking Management System**

**1. Objective**

To develop a Python-based car parking management system that manages parking slots, displays parking availability, allocates slots to vehicles, records entry and exit times, calculates parking charges, and releases parking slots.

**2. Input The program accepts:**

Menu choice
Vehicle number
Vehicle entry time
Vehicle exit time

The parking system uses:

Total parking slots: 100
Hourly parking rate: ₹50 per hour

**3. Output**

The program displays:

Total number of parking slots
Number of occupied slots
Number of available slots
Available slot numbers
Allocated parking slot
Vehicle number
Entry time
Exit time
Total parking duration
Parking charge
Parking receipt
Appropriate messages for full parking, already parked vehicles, unavailable vehicles, and invalid choices

**4. Algorithm**

1. Start.

2. Set the total number of parking slots to 100.

3. Set the parking rate to ₹50 per hour.

4. Create an empty dictionary to store occupied parking slots and vehicle details.

5. Display the parking management menu.

6. Read the user's choice.

7. If the choice is 1 (Show Availability), calculate the number of available slots by subtracting the occupied slots from the total slots.

8. Display the total number of parking slots.

9. Display the number of occupied slots.

10. Display the number of available slots.

11. If all slots are occupied, display "Parking is FULL!".

12. Otherwise, display the available slot numbers.

13. If the choice is 2 (Allocate Slot), check whether all parking slots are occupied.

14. If the parking is full, display "Parking is FULL. No slot available.".

15. Otherwise, read the vehicle number.

16. Convert the vehicle number to uppercase.

17. Check whether the vehicle is already parked.

18. If the vehicle is already parked, display "This vehicle is already parked.".

19. Otherwise, search for the first available parking slot.

20. Assign the vehicle to the available parking slot.

21. Record the current entry time.

22. Display the allocated slot number and entry time.

23. If the choice is 3 (Release Slot), read the vehicle number.

24. Search for the vehicle in the occupied parking slots.

25. If the vehicle is found, record the current exit time.

26. Calculate the parking duration using the entry time and exit time.

27. Round the parking duration up to the next complete hour.

28. Calculate the parking charge using:
    Parking Charge = Parking Hours × Hourly Rate

29. Display the parking receipt.

30. Display the vehicle number.

31. Display the slot number.

32. Display the entry time.

33. Display the exit time.

34. Display the parking duration.

35. Display the parking charge.

36. Release the occupied parking slot.

37. Display "Slot released successfully.".

38. If the vehicle is not found, display "Vehicle not found in the parking area.".

39. If the choice is 4 (Exit), display "Thank you!".

40. Terminate the program.

41. For any other choice, display "Invalid choice. Please try again.".

42. Repeat the menu until the user chooses Exit.

43. Stop.

**5. Time Complexity**

Let n be the number of occupied parking slots, where the maximum number of slots is 100.

Show Availability: O(100), which is effectively O(1) because the parking capacity is fixed.
Allocate Slot: O(n) for checking whether the vehicle is already parked and finding an available slot.
Release Slot: O(n) for searching for the vehicle.
Calculate Parking Charge: O(1)
Exit: O(1)

Therefore, the worst-case time complexity of a menu operation is O(n).

Since the maximum parking capacity is fixed at 100 slots, the practical maximum is bounded by a constant.

**6. Space Complexity**

O(n)

The parking dictionary stores the details of each occupied parking slot, including the vehicle number and entry time.
