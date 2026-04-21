# 🔹 Q2. Pandas – Missing Data Handling

# You are given a DataFrame with missing values:

# Fill numeric columns with median
# Fill categorical columns with mode
# Drop columns with >50% missing values



import pandas as pd

def clean_data(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col].fillna(df[col].mode()[0], inplace=True)
        else:
            df[col].fillna(df[col].median(), inplace=True)
    
    # Drop columns with >50% missing
    threshold = len(df) * 0.5
    df = df.dropna(axis=1, thresh=threshold)
    
    return df
