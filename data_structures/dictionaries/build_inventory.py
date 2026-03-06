# Build Inventory
# Write a function build_inventory() that takes in a list of product_names and a corresponding list of product_prices as parameters. The function returns a dictionary representing the inventory of a small store. Each product name in product_names should be a key in the dictionary and the corresponding value should be the item price.

# product_names[i] should be paired with product_prices[i] in the dictionary where 0 <= i <= len(product_names). You may assume that product_names and product_prices are the same length.

def build_inventory(product_names, product_prices):
    return {product_names[i]: product_prices[i] for i in range(len(product_names))}

product_names = ["Apple", "Banana", "Orange"]
product_prices = [0.99, 0.50, 0.75]
print(build_inventory(product_names, product_prices))