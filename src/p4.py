Problem 4 - Find List Intersection
Write a function that find the intersection between two lists.

List 1: 4, 5, 2, 3, 1, 6
List 2: 8, 7, 6, 9, 4, 5
Expected output: 4, 5, 6

Solution


def find_intersection(list1, list2):

    result = []

    # Compare each element in list1 with each element in list2
    for i in range(len(list1)):

        for j in range(len(list2)):

            # If matching element found
            if list1[i] == list2[j]:

                # Prevent duplicates in result
                already_exists = False

                # Check if element already added
                for k in range(len(result)):
                    if result[k] == list1[i]:
                        already_exists = True
                        break

                # Add only if not already present
                if not already_exists:
                    result.append(list1[i])

    return result


# Input given in lists
list1 = [4, 5, 2, 3, 1, 6]
list2 = [8, 7, 6, 9, 4, 5]

# Find intersection
intersection = find_intersection(list1, list2)

# Print result
print(", ".join(map(str, intersection)))



Bonus: Space-Time Complexity Analysis

Time Complexity

Nested loops: O(n×m)

where:
n = size of List 1
m = size of List 2

Space Complexity

O(r)

where:
r = number of intersecting elements stored in result list.











