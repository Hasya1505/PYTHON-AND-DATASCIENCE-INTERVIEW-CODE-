# 🔹 Q9. Pandas – Real Interview Scenario

# Given dataset of users:

# Find users who logged in 3 consecutive days

# 👉 Return user IDs

# 💡 Hint: use shift() or rolling window


def consecutive_logins(df):
    df = df.sort_values(['user_id', 'date'])
    
    df['prev1'] = df.groupby('user_id')['date'].shift(1)
    df['prev2'] = df.groupby('user_id')['date'].shift(2)
    
    df['diff1'] = (df['date'] - df['prev1']).dt.days
    df['diff2'] = (df['prev1'] - df['prev2']).dt.days
    
    result = df[(df['diff1'] == 1) & (df['diff2'] == 1)]
    
    return result['user_id'].unique()
