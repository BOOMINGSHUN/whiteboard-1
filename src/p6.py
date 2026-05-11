Problem 6 - Find Character with Maximum Occurence
Write a function that takes a string as input and finds the character that occurs the maximum number of times in the string. Return both the character and its occurrence count. If there are multiple characters with the same maximum occurrence, return any one of them.

Input: "Hello, world!"
Expected output: Character: 'l', Occurrence: 3


Solution:

Approach: Manually build a frequency table using a dictionary.
Steps:
1. Traverse each character in the string
2. Filter out: whitespace & punctuation
3. Count occurrences in a dictionary
4. Find the maximum frequency entry
5. Return result

Code

def max_occurrence_char(s):
    # DICTIONARY: Frequency Table
    # Purpose: stores each valid character as key and its occurrence count as value
    freq = {}

    # Step 1: Build frequency table
    for ch in s:

        # Ignore whitespace
        if ch.isspace():
            continue

        # Ignore punctuation (keep only alphanumeric / Unicode letters & digits)
        if not ch.isalnum():
            continue

        # If character already exists in dictionary, increment count
        if ch in freq:
            freq[ch] += 1
        else:
            # First time seeing this character → initialize count
            freq[ch] = 1

    # Step 2: Find character with maximum occurrence
    max_char = None
    max_count = 0

    for ch in freq:

        if freq[ch] > max_count:
            max_count = freq[ch]
            max_char = ch

    return max_char, max_count


# Input text
text = "Hello, world!"

# Print result
char, count = max_occurrence_char(text)

print(f"Character: '{char}', Occurrence: {count}")


Bonus: Handle Unicode Characters

The solution above already supports Unicode because:
1. Python strings are Unicode-based by default
2. dict keys can store Unicode characters
3. isalnum() supports Unicode letters/numbers

