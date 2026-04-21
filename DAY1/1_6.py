# 🔹 Q6. Python – String + HashMap (DSA Concept)
# Find the first non-repeating character in a string.
# 👉 Example: "aabbcde" → output: c
# 👉 Constraint: O(n) time


from collections import Counter

def first_unique(s):
    count = Counter(s)
    
    for char in s:
        if count[char] == 1:
            return char
    return None
