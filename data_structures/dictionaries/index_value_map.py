# Index-Value Map
# Write a function index_to_value_map() that takes in a list lst and returns a dictionary that maps the index of each element in lst to its value.

def index_to_value_map(lst):
    dictionary = {}

    for i in range(len(lst)):
        dictionary[i] = lst[i]

    return dictionary

lst = ["apple", "banana", "cherry"]
print(index_to_value_map(lst))
