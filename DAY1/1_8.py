# 🔹 Q8. NumPy + Performance Optimization

# Given large arrays:

# Compute dot product using NumPy
# Compare performance with Python loop

# 👉 Explain why NumPy is faster


import numpy as np

def dot_product():
    a = np.random.rand(1000000)
    b = np.random.rand(1000000)
    
    # NumPy
    result_np = np.dot(a, b)
    
    # Python loop
    result_py = 0
    for i in range(len(a)):
        result_py += a[i] * b[i]
    
    return result_np, result_py
