Problem 7 - Square Root
Write a function that calculates and returns the square root of a non-negative integer x. 
You can safely assume x is a perfect square, such as 4, 9, 16, 25, 36, and so on.


Idea:
By using Binary Search,
mid*mid = x

If:
mid^2 < x then move right
mid^2 > x then move left
equal then found answer

Example: x = 36

Search space: left = 1  right = 36
Step-by-step:
1. mid = 18 , 18² = 324 (too big, go left)
2. mid = 9 , 9² = 81 (too big, go left)
3. mid = 4 , 4² = 16 (too small, go right)
4. mid = 6 , 6² = 36  (found)

Code

def square_root(x):

    # Search range: 1 to x
    left = 1
    right = x

    while left <= right:

        mid = (left + right) // 2

        square = mid * mid

        # Found exact square root
        if square == x:
            return mid

        # Too small then move right
        elif square < x:
            left = mid + 1

        # Too large then move left
        else:
            right = mid - 1

    return -1  # fallback (not needed for perfect squares)


# Example input
x = 36

result = square_root(x)

print("Square root:", result)




Space-Time Complexity Analysis
Time Complexity: O(log n) where n=x

Space Complexity

No extra data structures used: O(1)
	​



