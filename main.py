import pandas as pd
from operator import itemgetter
import time

startTime = time.time()

# Importing and formating CSV datas to a list
data = pd.read_csv("Actions.csv")
actions = data.Action
prices = data.Prix
benefices = data.Benefice
formated_benefices = []

for benefice in benefices:
    formated_benefice = float(benefice.rstrip(benefice[-1]))
    formated_benefice = round(1 + (formated_benefice / 100), 2)
    formated_benefices.append(formated_benefice)

# Analyzing the actions to set a list of best return on investment
actions_revenus = []
for i in range(len(actions)):
    action = actions[i]
    price = prices[i]
    benefice = formated_benefices[i]
    final_value = round(price * benefice, 2)
    revenu = round(final_value - price, 2)
    roi = round(revenu / price, 3)
    action_summary = [action, price, benefice, final_value, revenu, roi]
    action_dictionary = {
        "action": action,
        "price": price,
        "benefice": benefice,
        "final_value": final_value,
        "revenu": revenu,
        "roi": roi,
    }
    actions_revenus.append(action_dictionary)
best_roi = sorted(actions_revenus, key=itemgetter("roi"), reverse=True)


# Applying the client criteria to the list of best ROI
# to deduce the list of action to buy
def getRois(List, budget):
    total_spent = 0
    action_to_buy = []
    for i in range(len(List)):
        action = List[i]
        price = action["price"]
        new_total = total_spent + price
        if new_total < budget:
            action_to_buy.append(action)
            total_spent += price
    return action_to_buy


# Exporting to CSV the list of best investment
best_actions = getRois(best_roi, 500)
analyzed_actions = pd.DataFrame.from_dict(best_actions)
analyzed_actions.to_csv("Action_analysis.csv", index=False, header=True)


endTime = time.time() - startTime

print(endTime)
