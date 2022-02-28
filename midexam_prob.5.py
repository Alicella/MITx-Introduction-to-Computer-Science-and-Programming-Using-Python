# Write a Python function that returns a list of keys in aDict with the value target. The list of keys you return should be sorted in increasing order. The keys and values in aDict are both integers. (If aDict does not contain the value target, you should return an empty list.)

# This function takes in a dictionary and an integer and returns a list.


def keysWithValue(aDict, target):
    '''
    aDict: a dictionary
    target: an integer
    '''
    # Your code here
    keys = []
    for k, v in aDict.items():
        if v == target:
            keys.append(k)
    keys.sort()
    return keys


dict = {1: 1, 9: 3, 3: 3, 5: 3}
print(keysWithValue(dict, 3))
