# Filter by price
# Write a function that takes in a dictionary of items and a price_threshold as parameters. The function should iterate through the dictionary and remove all items that has a value less than price_threshold. The function also returns a list of all items that are removed. If no item satisfies the condition, return None.

def remove_items_below_price(items, price_threshold):

    removed_items = []
    for item in items:
        if items[item] < price_threshold:
            removed_items.append(item)

    for item in removed_items:
        del items[item]

    if not removed_items:
        return None
    else:
        return removed_items

items = {"apple": 1.99, "banana": 0.99, "cherry": 3.49, "date": 0.69}
removed_list = remove_items_below_price(items, 1.00)
print(removed_list)
removed_list_two = remove_items_below_price(items, 1.00)
print(removed_list_two)