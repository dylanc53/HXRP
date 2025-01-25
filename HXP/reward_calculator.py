# utils/reward_calculator.py
def calculate_rewards(holders, total_rewards, daily_cap):
    """Calculate proportional rewards for each token holder."""
    total_balance = sum(holders.values())
    rewards = {}
    for holder, balance in holders.items():
        rewards[holder] = min((balance / total_balance) * total_rewards, daily_cap)
    return rewards
