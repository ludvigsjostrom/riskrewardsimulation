import random
import matplotlib.pyplot as plt
import numpy as np

def simulate_trading(starting_balance, number_of_trades, risk_reward_ratio, weight=1):
    balance = starting_balance
    balance_history = []
    for _ in range(number_of_trades):
        balance_change = risk_reward_ratio * weight if random.choices([True, False], weights=[1, weight])[0] else -risk_reward_ratio
        balance += balance * balance_change
        balance_history.append(balance)
    return balance_history

def average_trading_simulation(runs, starting_balance, number_of_trades, risk_reward_ratio, weight=1):
    all_simulations = [simulate_trading(starting_balance, number_of_trades, risk_reward_ratio, weight) for _ in range(runs)]
    return np.mean(np.array(all_simulations), axis=0)

# Parameters
runs = 1000
starting_balance = 100000
number_of_trades = 10000
risk_reward_ratios = [0.01, 0.01, 0.01, 0.01, 0.01]
weights = [1, 2, 3, 4, 5]

plt.figure(figsize=(12, 6))

for rr, weight in zip(risk_reward_ratios, weights):
    average_balances = average_trading_simulation(runs, starting_balance, number_of_trades, rr, weight)
    plt.plot(average_balances, linewidth=1, label=f'1:{weight} RR')

plt.title('Average Trader Balance Over 10000 Trades (1000 Simulations)', fontsize=14)
plt.xlabel('Number of Trades', fontsize=12)
plt.ylabel('Average Balance ($)', fontsize=12)
plt.grid(True, which='both', linestyle='--', linewidth=0.5, alpha=0.7)
plt.legend()
plt.tight_layout()
plt.show()
