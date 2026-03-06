# Sum even Values
# Write a function sum_even_values() that returns the sum of all even values in a given dictionary. Assume the dictionary values are all integers.

def sum_even_values(dictionary):
    
    return sum(value for value in dictionary.values() if value%2 == 0)

dictionary = {"a": 4, "b": 1, "c": 2, "d": 8, }
print(sum_even_values(dictionary))