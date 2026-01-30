# Menu Driven Program for Array Operations

def create_array():
    arr = []
    n = int(input("Enter number of elements: "))
    for i in range(n):
        value = int(input(f"Enter element {i + 1}: "))
        arr.append(value)
    return arr

def display_array(arr):
    print("\nArray elements are:")
    for i in arr:
        print(i, end=" ")
    print()

def insert_element(arr):
    value = int(input("Enter element to insert: "))
    arr.append(value)
    print("Element inserted successfully.")

def delete_element(arr):
    value = int(input("Enter element to delete: "))
    if value in arr:
        arr.remove(value)
        print("Element deleted successfully.")
    else:
        print("Element not found.")

def search_element(arr):
    value = int(input("Enter element to search: "))
    if value in arr:
        print(f"Element found at index {arr.index(value)}")
    else:
        print("Element not found.")

def array_statistics(arr):
    print("Maximum element:", max(arr))
    print("Minimum element:", min(arr))
    print("Sum of elements:", sum(arr))
    print("Average of elements:", sum(arr) / len(arr))

def sort_array(arr):
    print("Sorted array (Ascending):", sorted(arr))
    print("Sorted array (Descending):", sorted(arr, reverse=True))

# Main Program
array = create_array()

while True:
    print("\n----- ARRAY MENU -----")
    print("1. Display Array")
    print("2. Insert Element")
    print("3. Delete Element")
    print("4. Search Element")
    print("5. Array Statistics")
    print("6. Sort Array")
    print("7. Exit")

    choice = int(input("Enter your choice (1-7): "))

    if choice == 1:
        display_array(array)
    elif choice == 2:
        insert_element(array)
    elif choice == 3:
        delete_element(array)
    elif choice == 4:
        search_element(array)
    elif choice == 5:
        array_statistics(array)
    elif choice == 6:
        sort_array(array)
    elif choice == 7:
        print("Program terminated successfully.")
        break
    else:
        print("Invalid choice. Please try again.")
