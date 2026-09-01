**Car Parking Management System**

**1. Objective**

To develop a Python-based car parking management system that manages parking slots, displays parking availability, allocates slots to vehicles, records entry and exit times, calculates parking charges, and releases parking slots.

**2. Input**
The program accepts:

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

    Start.
    Set the total number of parking slots to 100.
    Set the parking rate to ₹50 per hour.
    Create an empty dictionary to store occupied parking slots and vehicle details.
    Display the parking management menu.
    Read the user's choice.
    If the choice is 1 (Show Availability):
        Calculate the number of available slots by subtracting the occupied slots from the total slots.
        Display the total number of slots.
        Display the number of occupied slots.
        Display the number of available slots.
        If all slots are occupied, display "Parking is FULL!".
        Otherwise, display the available slot numbers.
    If the choice is 2 (Allocate Slot):
        Check whether all parking slots are occupied.
        If parking is full, display "Parking is FULL. No slot available.".
        Otherwise, read the vehicle number.
        Convert the vehicle number to uppercase.
        Check whether the vehicle is already parked.
        If the vehicle is already parked, display "This vehicle is already parked.".
        Otherwise, search for the first available parking slot.
        Assign the vehicle to the available slot.
        Record the current entry time.
        Display the allocated slot number and entry time.
    If the choice is 3 (Release Slot):
        Read the vehicle number.
        Search for the vehicle in the occupied parking slots.
        If the vehicle is found:
            Record the current exit time.
            Calculate the parking duration using the entry and exit times.
            Round the parking duration up to the next complete hour.
            Calculate the parking charge using:
            Parking Charge = Parking Hours × Hourly Rate
            Display the parking receipt.
            Display the vehicle number.
            Display the slot number.
            Display the entry time.
            Display the exit time.
            Display the parking duration.
            Display the parking charge.
            Release the occupied parking slot.
            Display "Slot released successfully.".
        If the vehicle is not found, display "Vehicle not found in the parking area.".
    If the choice is 4 (Exit):
        Display "Thank you!".
        Terminate the program.
    For any other choice, display "Invalid choice. Please try again.".
    Repeat the menu until the user chooses Exit.
    Stop.

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
