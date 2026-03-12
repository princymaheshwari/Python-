# Good Pairs
# Write a function num_identical_pairs() that takes in a list of integers nums and returns the number of good pairs.
# A pair (i, j) is called good if nums[i] == nums[j] and i < j.

from collections import Counter
def num_identical_pairs(nums):

    frequency_map = Counter(nums)
    no_of_good_pairs = 0

    for frequency in frequency_map.values():
        no_of_good_pairs += frequency * (frequency -1 )//2

    return no_of_good_pairs


nums = [1,2,3,1,1,3]
print(num_identical_pairs(nums))

nums = [1,2,3]
print(num_identical_pairs(nums))

nums = [1,1,1,1]
print(num_identical_pairs(nums))
