# 🔹 Q10. Mixed (Python + DSA + Data Handling)

# You are given:

# A list of transactions (user_id, amount)

# Tasks:

# Find top 3 users by total spending
# Detect duplicate transactions
# Return users whose spending > average


from collections import defaultdict

def transaction_analysis(transactions):
    user_total = defaultdict(int)
    seen = set()
    duplicates = []
    
    # Total spending + duplicate detection
    for t in transactions:
        user, amount = t
        
        user_total[user] += amount
        
        if t in seen:
            duplicates.append(t)
        else:
            seen.add(t)
    
    # Top 3 users
    top_users = sorted(user_total.items(), key=lambda x: x[1], reverse=True)[:3]
    
    # Average spending
    avg = sum(user_total.values()) / len(user_total)
    
    above_avg = [user for user, total in user_total.items() if total > avg]
    
    return top_users, duplicates, above_avg
