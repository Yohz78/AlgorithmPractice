import pandas as pd
from operator import itemgetter
import time

startTime = time.time()

# Importing and formating CSV datas to a list
data = pd.read_csv("dataset2_Python.csv")
actions = data.name
initial_price = data.price
sell_price = data.profit


# Data preprocessing prior to analysis.
actions_revenus = []
for i in range(len(actions)):
    action = actions[i]
    price = float(initial_price[i])
    revenu = float(sell_price[i])
    final_price = price * (1 + (revenu / 100))
    gain = final_price - price
    if price > 0:
        action_dictionary = {
            "action": action,
            "price": price,
            "revenu": revenu,
            "gain": gain,
        }
        actions_revenus.append(action_dictionary)
sorted_actions = sorted(actions_revenus, key=itemgetter("revenu"), reverse=True)


# Work on the sorted list in order to deduce the best actions.
def getActions(List, budget):
    total_spent = 0
    action_to_buy = []
    total_gain = 0
    for i in range(len(List)):
        action = List[i]
        price = action["price"]
        new_total = total_spent + price
        if new_total < budget:
            gain = action["gain"]
            total_gain += gain
            action_to_buy.append(action)
            total_spent += price
    print(
        f"Le total dépensé est de {total_spent} le bénéfice total est de {total_gain}"
    )
    return action_to_buy


# Printing the list of best investment.
best_actions = getActions(sorted_actions, 500)
endTime = time.time() - startTime
print(f"L'application a mis {endTime} secondes à génerer le résultat.")
print("Les actions achetées sont :")
for action in best_actions:
    print(action["action"])
