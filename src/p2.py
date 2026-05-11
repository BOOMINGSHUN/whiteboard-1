Problem 2 - FizzBuzz
Given a list of ordered numbers from 1 to 100, perform the following actions

For every number divisible by 3, print 'Fizz'
For every number divisible by 5, print 'Buzz'
For every number divisible by both 3 and 5, print 'FizzBuzz'

Input: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, ..., 100
Expected output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz, 16, ..., 100


Solution

def fizz_buzz():
    
    # Store all outputs here
    result = []

    # Loop from 1 to 100
    for number in range(1, 101):

        # Check divisibility by both 3 and 5 first
        if number % 3 == 0 and number % 5 == 0:
            result.append("FizzBuzz")

        # Divisible by 3
        elif number % 3 == 0:
            result.append("Fizz")

        # Divisible by 5
        elif number % 5 == 0:
            result.append("Buzz")

        # Otherwise store the number as string
        else:
            result.append(str(number))

    # Join all elements
    print(", ".join(result))


# Run function
fizz_buzz()
