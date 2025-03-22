# filename: permutations.py
import math

def permutations_with_repetition(n, repetitions):
    """Calculates permutations with repetitions.

    Args:
        n: The total number of items.
        repetitions: A dictionary where keys are items and values are their counts.

    Returns:
        The number of permutations.
    """

    numerator = math.factorial(n)
    denominator = 1
    for count in repetitions.values():
        denominator *= math.factorial(count)
    return numerator // denominator

n = 7  # Total number of letters
repetitions = {'A': 2} # Occurrences of the repeated letters

result = permutations_with_repetition(n, repetitions)
print(result)

