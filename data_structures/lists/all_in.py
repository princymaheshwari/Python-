# All In
# Write a function all_in() that takes in a list of integers a and a list of integers b as parameters. Given these two lists, return True if every element in list a is in list b. Return False otherwise.

def all_in(a, b):

    common_elements = []
    
    for element_a in a:
        for element_b in b:
            if element_a == element_b:
                common_elements.append(element_b)

    if a == common_elements:
        return True
    else:
        return False

list1 = [1, 2]
list2 = [1, 2, 3]
print(all_in(list1, list2))
print(all_in(list2, list1))