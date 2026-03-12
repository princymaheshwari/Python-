# Find Mode
# Write a function find_mode() that takes in a non-empty list of integers lst as a parameter. The function returns the mode (the most frequently occurring number) and if there is a tie, return the element which appeared first in the list.
from collections import Counter

def find_mode(lst):
    frequency_map = dict(Counter(lst))
    max_frequency = max(frequency_map.values())

    for num in lst:
        if frequency_map[num] == max_frequency:
            return num

lst = [1,2,3,2,3,3,4,4,4,4]
mode = find_mode(lst)
print(mode)