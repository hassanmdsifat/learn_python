item_prices = [10, 20, 100, 500, 600]
total_budget = 500
# 990 970 870 370
total_count = 0

for current_item_price in item_prices:
    total_budget -= current_item_price
    if total_budget < 0:
        break
    total_count += 1

print(total_count)