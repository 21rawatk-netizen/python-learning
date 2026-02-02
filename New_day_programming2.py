# Array (List) Operations in Python

def array_operations(arr):
    print("Original Array:", arr)
    print("Length of array:", len(arr))
    print("Maximum element:", max(arr))
    print("Minimum element:", min(arr))
    print("Sum of elements:", sum(arr))
    print("Sorted array:", sorted(arr))
    print("Reversed array:", arr[::-1])


# Taking user input
n = int(input("Enter number of elements: "))
array = []

for i in range(n):
    value = int(input(f"Enter element {i + 1}: "))
    array.append(value)

array_operations(array)
