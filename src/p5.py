Problem 5 - Find List Symmetric Difference
Write a function that find the symmetric difference between two lists.

List 1: 4, 5, 2, 3, 1, 6
List 2: 8, 7, 6, 9, 4, 5
Expected output: 1, 2, 3, 7, 8, 9


Solution:

Definition: The symmetric difference between two sets/lists.
Approach
1. Check elements in List 1 not found in List 2
2. Check elements in List 2 not found in List 1
3. Combine both results
4. Avoid duplicates

Code

def symmetric_difference(list1, list2):

    result = []

    # Part 1: Elements in list1 but not in list2
    for i in range(len(list1)):

        found = False

        for j in range(len(list2)):
            if list1[i] == list2[j]:
                found = True
                break

        # If not found in list2, it's unique
        if not found:
            # Prevent duplicates in result
            already_exists = False

            for k in range(len(result)):
                if result[k] == list1[i]:
                    already_exists = True
                    break

            if not already_exists:
                result.append(list1[i])

    # Part 2: Elements in list2 but not in list1
    for i in range(len(list2)):

        found = False

        for j in range(len(list1)):
            if list2[i] == list1[j]:
                found = True
                break

        # If not found in list1, it's unique
        if not found:

            # Prevent duplicates in result
            already_exists = False

            for k in range(len(result)):
                if result[k] == list2[i]:
                    already_exists = True
                    break

            if not already_exists:
                result.append(list2[i])

    return result

# Selection Sort (manual sorting)
def selection_sort(arr):

    n = len(arr)

    for i in range(n):

        min_index = i

        for j in range(i + 1, n):

            if arr[j] < arr[min_index]:
                min_index = j

        # Swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr

# Input lists
list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]

# Step 1: Get symmetric difference
result = symmetric_difference(list1, list2)

# Step 2: Sort result in ascending order
sorted_result = selection_sort(result)

# Print final output
print(", ".join(map(str, sorted_result)))













