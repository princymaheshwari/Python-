# Dictionary Intersection
# Write a function dict_intersection() that takes in two dictionaries as parameters and returns a new dictionary containing the key-value pairs found in both dictionaries.

def dict_intersection(d1, d2):

    return {key: value for key, value in d1.items() if key in d2 and d2[key]==value}

d1 = {'a': 1, 'b': 2, 'c': 3}
d2 = {'b': 2, 'c': 4}

print(dict_intersection(d1, d2))