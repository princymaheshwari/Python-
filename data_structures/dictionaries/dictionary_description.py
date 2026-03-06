# Dictionary Description
# The following function get_description() takes in a dictionary info and a list keys as parameters. For each key in keys, the function prints the value associated with that key in info and prints None if the key does not exist in info.

def get_description(info, keys):

    for key in keys:
        if key in info.keys():
            print(info[key])
        else:
            print("None")

info = {"name": "Tom", "age": "30", "occupation": "engineer"}
keys = ["name", "occupation", "salary"]
get_description(info, keys)
