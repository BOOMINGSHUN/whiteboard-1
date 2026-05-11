Problem 1 - Sorting

Given a list of random unordered numbers, write a function that sort them in ascending order.
Input: 21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28
Expected output: -36, -16, -3, 8, 21, 28, 55, 77, 99, 111, 400


Solution

Method: Merge Sort

Code:

def merge_sort(arr):

    # Base case:
    # If the array has 0 or 1 element, it is already sorted.
    if len(arr) <= 1:
        return arr

    # Find the middle index
    mid = len(arr) // 2

    # Divide the array into left half and right half
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort both half 
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_sorted, right_sorted)

# Function for Merges two sorted arrays into one sorted array.
def merge(left, right):

    merged = []
    i = 0  # Pointer for left array
    j = 0  # Pointer for right array

    # Compare elements from both arrays and insert the smaller one into merged array
    while i < len(left) and j < len(right):

        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining elements from left array
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Add remaining elements from right array
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged


# Input data
numbers = [21, 400, 8, -3, 77, 99, -16, 55, 111, -36, 28]

# Perform sorting
sorted_numbers = merge_sort(numbers)

# Print result
print(sorted_numbers)



