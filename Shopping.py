# Write a Python program (Shopping.py) that reads data from multiple data files stored 
# within a folder whose name will be provided in the command line. 
# The program should process the data to provide answers to questions about the data.

#Step 1: Import all the libraries used

import sys
import glob

# Step 2: Making the function to read all data

def read_data():
    folder_name = sys.argv[1]

    # Extracting all files in the folder name that we input in the command line that end with .dat
    files = sorted(glob.glob(f"{folder_name}/*.dat"))
    invoices = []

    # Setting up a for loop that adds each invoice to the invoices list when run

    for filename in files:

        # Reading each file
        with open(filename, 'r') as f:

            # Splitting the lines
            lines_invoice = f.read().splitlines()

            # Dealing with the header line

            header_line = lines_invoice[0]
            header_line_parts = header_line.split(",")
            invoice_no = header_line_parts[0]
            store_name = header_line_parts[1]
            customer_name = header_line_parts[2]

            # Making a list of tuples of items

            item_lines = lines_invoice[1:]
            items = []
            for line in item_lines:
                item_parts = line.split(",")
                name_of_item, category_of_item, quantity_purchased, price_per_unit = item_parts
                items.append((name_of_item, category_of_item, float(quantity_purchased), float(price_per_unit)))

        # Making a tuple for each invoice

        invoice = (invoice_no, store_name, customer_name, items)

        # Adding each invoice in the invoices list
        invoices.append(invoice)
    
    return invoices

# Step 3: Making the function to see all customers

def get_all_customers(invoices):
    # Making an empty set as objects can't be repeated in a set
    customer_names = set()
    for invoice in invoices:
        customer = invoice[2]
        customer_names.add(customer)
        # Sorting customer names in alphabetical order
    customer_names = sorted(customer_names)
    # Printing customer names individually by the for loop and not in a set form
    for name in customer_names:
        print(name)

# Step 4: Making the Function to see all stores

def get_all_stores(invoices):
    # Making an empty set as objects can't be repeated in a set
    store_names = set()
    for invoice in invoices:
        store = invoice[1]
        store_names.add(store)
        # Sorting store names in alphabetical order
    store_names = sorted(store_names)
    # Printing store names individually by the for loop and not in set form
    for name in store_names:
        print(name)


# Step 5: Making a function to see all categories

def get_all_categories(invoices):
    categories = set()
    for invoice in invoices:
        items = invoice[3]

        for item in items:
            category = item[1]
            categories.add(category)
    
    categories = sorted(categories)
    for name in categories:
        print(name)

# Step 6: Making a function that, given a customer, returns a list of expenditures per store for that customer

def customer_spend_per_store(invoices, customer_name):
    # Initialize a dictionary to store the total spent per store
    spend_per_store = {}

    # Go through every invoice
    for invoice in invoices:
        store = invoice[1]
        customer = invoice[2]
        items = invoice[3]

        if store not in spend_per_store:
            spend_per_store[store] = 0.0

        # Add total spend for this customer at this store
        if customer == customer_name:
            for item in items:
                quantity = item[2]
                price = item[3]
                spend_per_store[store] += quantity * price
    # Print results
    print(f"\n{customer_name} spend per store:\n")
    for store, total in sorted(spend_per_store.items()):
        print(f"{store:<15}\t{total:>8.1f}")

# Step 7: Making a function to see loyal customers (customers who purchase only from one store)

def loyal(invoices):
    customer_stores = {}

    for invoice in invoices:
        store = invoice[1]
        customer = invoice[2]

        if customer not in customer_stores:
            customer_stores[customer] = set()
        customer_stores[customer].add(store)

    print("\nLoyal customers:\n")
    for customer, stores in sorted(customer_stores.items()):
        if len(stores) == 1:
            print(customer)

# Step 8: Main program logic

def main():
    if len(sys.argv) < 2:
        print("Usage: python Shopping.py <folder_name>")
        sys.exit(1)

    invoices = read_data()

    print("\nWelcome to Shopping Program\n")

    while True:
        print("See all customers (c)")
        print("See all stores (s)")
        print("See all categories (g)")
        print("See customer purchases at various stores (p cname)")
        print("See loyal customers (y)")
        print("Quit (q)\n")

        user_input = input("What do you want to see? ").strip().split()

        if not user_input:
            print("\nInvalid command\n")
            continue

        command = user_input[0]

        if command == "c":
            print("\nCustomers:\n")
            get_all_customers(invoices)

        elif command == "s":
            print("\nStores:\n")
            get_all_stores(invoices)

        elif command == "g":
            print("\nCategories:\n")
            get_all_categories(invoices)

        elif command == "p":
            if len(user_input) < 2:
                print("\nPlease provide a customer name.\n")
            else:
                customer_name = " ".join(user_input[1:])
                customer_spend_per_store(invoices, customer_name)

        elif command == "y":
            loyal(invoices)
    

        elif command == "q":
            print("\nBye!\n")
            break

        else:
            print("\nInvalid command\n")


if __name__ == "__main__":
    main()




      
