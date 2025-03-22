# filename: permutation_count.py

import math

def factorial(n):
    """Calculate n!"""
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def unique_permutations(word):
    """Return the number of unique permutations of a word"""
    # Convert to lower case and count frequency of each letter
    freq = {}
    for char in word.lower():
        if char.isalpha():  # Ignore non-alphabetic characters
            freq[char] = freq.get(char, 0) + 1

    # Calculate the total number of permutations using factorials and division
    num_permutations = math.factorial(len(word))
    for count in freq.values():
        num_permutations //= math.factorial(count)

    return num_permutations


print(unique_permutations('ALGEBRA'))