# filename: permutations_count.py
import itertools

def count_permutations(word):
    # Generate all permutations
    permutations = itertools.permutations(word)
    # Convert to a set to remove duplicates
    unique_permutations = set(permutations)
    # Count the number of unique permutations
    count = len(unique_permutations)
    print(f"The number of unique permutations of the word '{word}' is: {count}")

# Word to permute
word = "ALGEbRA"
count_permutations(word)