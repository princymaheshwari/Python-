# Find Unique Items
# Write a function find_unique_items() that takes two lists list_a and list_b as parameters. The function identifies unique items from the lists and returns a dictionary with the items as keys and a boolean value as the value indicating whether the item is unique to the first list (True) or not (False).

def find_unique_items(list_a, list_b):

    unique_items={}

    for item in list_a:
        if item not in list_b:
            unique_items[item] = True

    for item in list_b:
        if item not in list_a:
            unique_items[item] = False

    return unique_items

list_a = ["apple", "banana", "carrot"]
list_b = ["apple", "banana", "date"]
print(find_unique_items(list_a, list_b))