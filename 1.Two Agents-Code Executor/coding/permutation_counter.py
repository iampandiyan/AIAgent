# filename: permutation_counter.py
import math

def count_unique_permutations(word):
    """
    Calculates the number of unique permutations of a given word.

    Args:
        word: The input word (string).

    Returns:
        The number of unique permutations (integer).
    """

    char_counts = {}
    for char in word:
        char_counts[char] = char_counts.get(char, 0) + 1

    n = len(word)
    denominator = 1
    for count in char_counts.values():
        denominator *= math.factorial(count)

    return math.factorial(n) // denominator



print(count_unique_permutations('ALGEBRA'))
