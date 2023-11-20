import random
import matplotlib.pyplot as plt
import numpy as np

def simulate_trading(starting_balance, number_of_trades, risk_reward_ratio):
    balance = starting_balance
    balance_history = []
    for _ in range(number_of_trades):
        balance += balance * (2 * risk_reward_ratio if random.choices([True, False], weights=[1, 2])[0] else -risk_reward_ratio)
        balance_history.append(balance)
    return balance_history

def average_trading_simulation(runs, starting_balance, number_of_trades, risk_reward_ratio):
    all_simulations = [simulate_trading(starting_balance, number_of_trades, risk_reward_ratio) for _ in range(runs)]
    return np.mean(np.array(all_simulations), axis=0)

average_balances = average_trading_simulation(1000, 100000, 10000, 0.01)
average_balance = np.mean(average_balances)
max_balance = np.max(average_balances)
min_balance = np.min(average_balances)

average_balance, max_balance, min_balance

plt.figure(figsize=(12, 6))
plt.plot(average_balances, color='000000', linewidth=1)
plt.title('Average Trader Balance Over 10000 Trades (1000 Simulations) 1:2 RR', fontsize=14)
plt.xlabel('Number of Trades', fontsize=12)
plt.ylabel('Average Balance ($)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()
