# Frequency Count
# Write a function that takes in a list of integers nums and counts the number of occurrences of each integer. The function returns the result as a dictionary with integers as keys and their counts as values.

from collections import Counter

def count_occureneces(nums):

    return dict(Counter(nums))

nums = [1, 2, 2, 3, 3, 3, 4]
print(count_occureneces(nums))