# 🔹 Q5. Seaborn – Data Visualization Insight

# Using Seaborn:

# Create heatmap of correlation matrix
# Highlight highly correlated features (>0.8)

# 👉 Explain what insights can be derived


import seaborn as sns
import matplotlib.pyplot as plt

def correlation_heatmap(df):
    corr = df.corr()
    
    sns.heatmap(corr, annot=True, cmap='coolwarm')
    plt.show()
    
    # Extract highly correlated pairs
    high_corr = corr[(corr > 0.8) & (corr < 1.0)]
    return high_corr
