# Q3. Pandas – GroupBy + Aggregation

# Given sales data:

# Group by region and product
# Calculate:
# total revenue
# average sales
# max transaction

def sales_analysis(df):
    result = df.groupby(['region', 'product']).agg(
        total_revenue=('revenue', 'sum'),
        avg_sales=('revenue', 'mean'),
        max_transaction=('revenue', 'max')
    ).reset_index()
    
    return result.sort_values(by='total_revenue', ascending=False)
