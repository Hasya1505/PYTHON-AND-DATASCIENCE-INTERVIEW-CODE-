# 🔹 Q4. Matplotlib – Multi-Plot Visualization

# Create a function that:

# Plots:
# Line plot (trend)
# Bar chart (comparison)
# Histogram (distribution)
# All in a single figure


import matplotlib.pyplot as plt

def plot_all(data):
    fig, axs = plt.subplots(1, 3, figsize=(15, 5))
    
    # Line plot
    axs[0].plot(data)
    axs[0].set_title("Line Plot")
    
    # Bar chart
    axs[1].bar(range(len(data)), data)
    axs[1].set_title("Bar Chart")
    
    # Histogram
    axs[2].hist(data)
    axs[2].set_title("Histogram")
    
    plt.show()
