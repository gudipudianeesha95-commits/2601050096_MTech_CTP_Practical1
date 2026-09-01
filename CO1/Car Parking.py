from datetime import datetime

TOTAL_SLOTS = 100
HOURLY_RATE = 50  # ₹50 per hour

# Dictionary to store occupied slots
# Key = slot number, Value = vehicle details
parking_slots = {}


def show_availability():
    """Display available and occupied parking slots."""
    available = TOTAL_SLOTS - len(parking_slots)

    print("\n--- Parking Availability ---")
    print(f"Total slots    : {TOTAL_SLOTS}")
    print(f"Occupied slots : {len(parking_slots)}")
    print(f"Available slots: {available}")

    if available == 0:
        print("Parking is FULL!")

    else:
        print("Available slot numbers:")
        for slot in range(1, TOTAL_SLOTS + 1):
            if slot not in parking_slots:
                print(slot, end=" ")
        print()


def allocate_slot():
    """Allocate the first available slot to a vehicle."""
    if len(parking_slots) == TOTAL_SLOTS:
        print("\nParking is FULL. No slot available.")
        return

    vehicle_number = input("Enter vehicle number: ").strip().upper()

    # Check whether vehicle is already parked
    for details in parking_slots.values():
        if details["vehicle"] == vehicle_number:
            print("This vehicle is already parked.")
            return

    # Find first available slot
    for slot in range(1, TOTAL_SLOTS + 1):
        if slot not in parking_slots:
            parking_slots[slot] = {
                "vehicle": vehicle_number,
                "entry_time": datetime.now()
            }

            print(f"\nVehicle {vehicle_number} allocated to slot {slot}.")
            print(f"Entry time: {parking_slots[slot]['entry_time']}")
            return


def calculate_charge(entry_time, exit_time):
    """Calculate parking charge based on parking duration."""
    duration = exit_time - entry_time

    # Convert seconds to hours and round up
    hours = max(1, (duration.total_seconds() + 3599) // 3600)

    charge = int(hours * HOURLY_RATE)

    return int(hours), charge


def release_slot():
    """Release a vehicle's parking slot and calculate its charge."""
    vehicle_number = input("Enter vehicle number: ").strip().upper()

    for slot, details in parking_slots.items():
        if details["vehicle"] == vehicle_number:
            exit_time = datetime.now()

            hours, charge = calculate_charge(
                details["entry_time"],
                exit_time
            )

            print("\n--- Parking Receipt ---")
            print(f"Vehicle number : {vehicle_number}")
            print(f"Slot number    : {slot}")
            print(f"Entry time     : {details['entry_time']}")
            print(f"Exit time      : {exit_time}")
            print(f"Parking time   : {hours} hour(s)")
            print(f"Parking charge : ₹{charge}")

            # Release the slot
            del parking_slots[slot
-1
            print("Slot released successfully.")
            return

    print("Vehicle not found in the parking area.")


def main():
    """Main menu."""
    while True:
        print("\n===== PARKING MANAGEMENT SYSTEM =====")
        print("1. Show availability")
        print("2. Allocate slot")
        print("3. Release slot")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            show_availability()

        elif choice == "2":
            allocate_slot()

        elif choice == "3":
            release_slot()

        elif choice == "4":
            print("Thank you!")
            break

        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main()
