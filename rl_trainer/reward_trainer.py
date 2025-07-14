import pandas as pd

def calculate_reward(rating, edit_distance):
    # Simple weighted reward function
    return (rating * 2) - (edit_distance * 10)

# Load feedback log
df = pd.read_csv("feedback_log.csv")

# Calculate reward for each entry
df['reward'] = df.apply(lambda row: calculate_reward(row['human_rating'], row['edit_distance']), axis=1)

# Print rewards per chapter
print(df[['chapter', 'reward']])

# Save for future training
df.to_csv("feedback_log_with_rewards.csv", index=False)
print("Rewards saved to feedback_log_with_rewards.csv")
