# Find Odd Occurences
# Write a function find_odd_occurrences() that takes in a list of integers numbers where all numbers occur an even number of times except for two unique numbers that occur an odd number of times. The function should find the two unique numbers and return them as a list. Assume each problem has exactly one solution.

from collections import Counter
def find_odd_occurrences(numbers):

    frequency_map = dict(Counter(numbers))
    return [number for number, frequency in frequency_map.items() if frequency%2 != 0]

numbers = [1,4,2,3,2,3,3,4,4,4]
odd_list = find_odd_occurrences(numbers)
print(odd_list)