# Make Pairs
# Write a function divide_list() that takes in an integer list nums consisting of 2*n integers as parameters. The function divides nums into n pairs such that:

# Each element belongs to exactly one pair
# The elements present in a pair are equal
# Return True if nums can be divided into n pairs, otherwise return False.

from collections import Counter
def divide_list(nums):

    frequency_map = dict(Counter(nums))
    for frequency in frequency_map.values():
        if frequency % 2 != 0:
            return False
        
    return True

nums = [3,2,3,2,2,2]
print(divide_list(nums))

nums = [1,2,3,4]
print(divide_list(nums))
