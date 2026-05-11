Problem 3 - Fibonacci Sequence
Write a function that generate Fibonacci sequence using recursion technique. Allow the user to specify the number of Fibonacci sequence elements to generate.

Expected output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...


Solution

Fibonacci Definition

F(n) = F(n−1) + F(n−2) with base cases: F(0) = 0 F(1) = 1

Code

def fibonacci(n):

    # Base case 1
    if n == 0:
      return 0

    # Base case 2
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def generate_fibonacci_sequence(count):

    result = []

    # Generate each Fibonacci number
    for i in range(count):
        result.append(str(fibonacci(i)))

    print(", ".join(result))


# Ask user how many elements to generate
num = int(input("Enter number: "))

# Generate sequence
generate_fibonacci_sequence(num)



Bonus: To prevent stack overflow, use an iterative approach instead of recursion.

Code (Iterative Approach)

def fibonacci_iterative(count):

    a = 0
    b = 1

    result = []

    for _ in range(count):

        result.append(str(a))

        # Update Fibonacci values
        a, b = b, a + b

    print(", ".join(result))

fibonacci_iterative(10)
