# Mountain Peak
# A mountain list is defined as a list that has at least three elements, where there exists some i with 0 < i < len(lst)-1 such that lst[0] < lst[1] < ... lst[i-1] < lst[i] and lst[i] > lst[i+1] > ... > lst[len(lst)-1].

def peak_index_in_mountain_list(lst):

    left = 0
    right = len(lst) -1

    while right > left:
        mid = (left+right) //2

        if lst[mid] > lst[mid+1]:
            right = mid
        elif lst[mid+1] > lst[mid]:
            left = mid+1

    return left

mountain_lst = [0,3,8,0]
peak = peak_index_in_mountain_list(mountain_lst)
print(peak)