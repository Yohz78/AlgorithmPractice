import pandas as pd
import time
import itertools

startTime = time.time()

# Importing and formating CSV datas to a list
data = pd.read_csv("Actions.csv")
actions = data.name
initial_price = data.price
sell_price = data.profit

# Analyzing the actions to set a list of best return on investment
actions_revenus = []
for i in range(len(actions)):
    action = actions[i]
    price = float(initial_price[i])
    revenu = float(sell_price[i])
    final_price = price * (1 + (revenu / 100))
    gain = final_price - price
    if price > 0:
        action_summary = [action, price, revenu, gain]
        actions_revenus.append(action_summary)

# Brute Force Algorithm
buyable_combination = []
gain = 0
cost = 0
for i in range(len(actions_revenus)):
    combinations = list(itertools.combinations(actions_revenus, i))
    for j in range(len(combinations)):
        combination_test = combinations[j]
        actions_prices = [action[1] for action in combination_test]
        if sum(actions_prices) < 500:
            combination_gain = sum([action[3] for action in combination_test])
            if combination_gain > gain:
                cost = sum(actions_prices)
                gain = combination_gain
                best_combination = combination_test


endTime = time.time() - startTime
print(f"La meilleure combinaison coûte {cost} pour un gain total de {gain}.")
print(f"L'application a mis {endTime} secondes à génerer le résultat.")
print("Les actions achetées sont :")
for action in best_combination:
    print(action["action"])
