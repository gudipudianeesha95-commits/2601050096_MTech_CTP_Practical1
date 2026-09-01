def binary_search(books, target):
    low = 0
    high = len(books) - 1

    while low <= high:
        mid = (low + high) // 2

        if books[mid] == target:
            return mid + 1       # Location (1-based position)

        elif books[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1                    # Book not found


# Books arranged from 1 to 10 lakh
books = list(range(1, 1000001))

target = 75000

position = binary_search(books, target)

if position != -1:
    print("Book exists.")
    print("Book number:", target)
    print("Location/Position:", position)
else:
    print("Book does not exist.")