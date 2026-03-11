# Find Majority Element
# Write a function find_majority_element() that takes in a list of integers elements and finds the majority element in the list. A majority element is an element that appears more than n/2 times where n is the size of the list. If there is no majority element, return None.

from collections import Counter

def find_majority_element(elements):

    frequency_map = dict(Counter(elements))
    return next((element for element, frequency in frequency_map.items() if frequency> (len(elements)/2)), None)

elements = [2, 2, 1, 1, 1, 2, 2]
print(find_majority_element(elements))