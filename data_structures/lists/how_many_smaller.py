# How many smaller
# Write a function smaller_numbers_than_current() that takes in a list of numbers nums as a parameter. For each nums[i], the function should find out how many numbers in the list are smaller than it. (For each nums[i], count the number of valid j's such that j!=i and nums[j] < nums[i])

def smaller_numbers_than_current(nums):

    output_list = []
    for i in range(len(nums)):

        count = 0
        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1

        output_list.append(count)

    return output_list

nums = [6,1,2,2,3]
print(smaller_numbers_than_current(nums))