# Odd keys Even Values
# Write a function odd_keys_even_values() that takes in dictionary as a parameter, a dictionary with integer keys and values. The function returns a list of keys that are odd where their corresponding values are even.

def odd_keys_even_values(dictionary):

    return list(keys for keys, values in dictionary.items() if keys%2 != 0 and values%2 == 0)

dictionary = {1: 2, 2: 6, 3: 5, 4: 4, 5: 8}
final_list = odd_keys_even_values(dictionary)
print(final_list)