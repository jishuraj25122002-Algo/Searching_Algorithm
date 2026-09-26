def ternarySearch(arr, i, j, key):

    # Base condition
    if i > j:
        return -1

    # Find two middle positions
    mid1 = i + (j - i) // 3
    mid2 = j - (j - i) // 3

    # Check first middle element
    if arr[mid1] == key:
        return mid1

    # Check second middle element
    elif arr[mid2] == key:
        return mid2

    # Search in the first third
    elif key < arr[mid1]:
        return ternarySearch(arr, i, mid1 - 1, key)

    # Search in the third third
    elif key > arr[mid2]:
        return ternarySearch(arr, mid2 + 1, j, key)

    # Search in the middle third
    else:
        return ternarySearch(arr, mid1 + 1, mid2 - 1, key)


# Driver code

arr = []

n = int(input("Enter the number of elements: "))

for i in range(n):
    ele = int(input("Enter the element: "))
    arr.append(ele)

# Ternary search requires sorted array
arr.sort()

key = int(input("Enter the number to search: "))

# Function calling
result = ternarySearch(arr, 0, len(arr) - 1, key)

print("Sorted array:", arr)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")