# Update or Warn
# Write a function update_or_warn() that takes in a dictionary records, a key item, and a new value update_value as parameters. The function updates the value of item in records with update_value if item exists. If item does not exist, it should print "<item> not found!" and not modify the dictionary.

def update_or_warn(records, item, update_value):

    if item in records:
        records[item] = update_value
    else:
        print(f"{item} not found!")

    return records


records = {"apple": 1, "banana": 2, "orange": 3}
update_or_warn(records, "grape", 4)
# Print the input dictionary after running the function to check if it was modified
print(records) 
update_or_warn(records, "banana", 5)
print(records)