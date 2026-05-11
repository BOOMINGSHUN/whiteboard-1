Problem 8 - Anagram Checker
Write a function that takes two strings as input and checks if they are anagrams of each other. 
Anagrams are words or phrases formed by rearranging the letters of another word or phrase.

Solution:

Approach: Use a frequency dictionary (hash map)
Steps:
1. Normalize both strings: convert to lowercase, remove whitespace, remove punctuation
2. Count frequency of each character in first string
3. Subtract frequency using second string
4. If all counts become zero → anagram

Code

def clean_string(s):

    cleaned = ""

    for ch in s:

        # Ignore whitespace
        if ch.isspace():
            continue

        # Ignore punctuation (keep only alphanumeric)
        if not ch.isalnum():
            continue

        # Convert to lowercase and keep character
        cleaned += ch.lower()

    return cleaned


def is_anagram(s1, s2):

    s1 = clean_string(s1)
    s2 = clean_string(s2)

    # If lengths differ after cleaning → not anagrams
    if len(s1) != len(s2):
        return False

    # Frequency dictionary
    freq = {}

    # Count characters in first string
    for ch in s1:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

    # Subtract counts using second string
    for ch in s2:

        if ch not in freq:
            return False

        freq[ch] -= 1

    # Check if all counts are zero
    for value in freq.values():
        if value != 0:
            return False

    return True


# Test/Show result
print(is_anagram("Conversation", "Voices, rant on"))



Bonus: Space-Time Complexity Analysis

Time Complexity
Let: n = length of cleaned string

Cleaning step: O(n)
Frequency build: O(n)
Frequency check: O(n)
Total: O(n)

Space Complexity

O(k) , where k = number of distinct characters

























