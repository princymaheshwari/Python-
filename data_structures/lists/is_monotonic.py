# Is Monotonic
# Write a function is_monotonic() that takes in a list nums as a parameter and checks if it is either monotone increasing or monotone decreasing.
# A list is monotone increasing if every element is either greater than or equal to the element before it.
# A list is monotone decreasing if every element is either less than or equal to the element before it.
# The function should return True if the given list is either monotone increasing or decreasing and False otherwise.

def is_monotonic(nums):
    
    is_increasing = True
    is_decreasing = True

    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            is_decreasing = False
        if nums[i] > nums[i+1]:
            is_increasing = False

    return is_increasing or is_decreasing
  

nums1 = [1,2,2,3,10]
print(is_monotonic(nums1))

nums2 = [12,9,8,3,1]
print(is_monotonic(nums2))

nums3 = [1,1,1]
print(is_monotonic(nums3))

nums4 = [1,9,8,3,5]
print(is_monotonic(nums4))