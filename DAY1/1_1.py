# Q1. NumPy – Advanced Array Manipulation

# Given a NumPy array of shape (n, m), write a function to:

# Normalize each row (mean = 0, std = 1)
# Handle division-by-zero safely

import numpy as np

def normalize_rows(arr):
    mean = np.mean(arr, axis=1, keepdims=True)
    std = np.std(arr, axis=1, keepdims=True)
    
    # Avoid division by zero
    std[std == 0] = 1
    
    normalized = (arr - mean) / std
    return normalized
