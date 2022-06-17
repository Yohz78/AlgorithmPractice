import pandas as pd
from operator import itemgetter
import time

startTime = time.time()

# Importing and formating CSV datas to a list
data = pd.read_csv("dataset2_Python.csv")
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
        roi = round(revenu / price, 3)
        action_summary = [action, price, revenu, roi]
        action_dictionary = {
            "action": action,
            "price": price,
            "revenu": revenu,
            "roi": roi,
            "gain": gain,
        }
        actions_revenus.append(action_dictionary)
best_roi = sorted(actions_revenus, key=itemgetter("revenu"), reverse=True)


# Applying the client criteria to the list of best ROI
# to deduce the list of action to buy
def getRois(List, budget):
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


# Exporting to CSV the list of best investment
best_actions = getRois(best_roi, 500)
analyzed_actions = pd.DataFrame.from_dict(best_actions)
analyzed_actions.to_csv("Action_analysis.csv", index=False, header=True)


endTime = time.time() - startTime

print(endTime)
