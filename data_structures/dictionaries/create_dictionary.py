# Write a function create_dictionary() that takes in a list of keys and a list of values as parameters. The function returns a dictionary where each item in keys is paired with a corresponding item in values.

def create_dictionary(keys, values):

    dictionary = {}
    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]

    return dictionary

keys = ['peanut', 'dragon', 'star', 'pop', 'space']
values = ['butter', 'fly', 'fish', 'corn', 'ship']
print(create_dictionary(keys, values))