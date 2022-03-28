def uniqueValues(aDict):
    '''
    aDict: a dictionary
    returns: a sorted list of keys that map to unique aDict values, empty list if none
    '''

    new_dict = {}
    # loop in the dict, by the end should return new dict with distinct value/key pairs vs. adict
    for k, v in aDict.items():
        # if the value hasn't occurred before, add to new dict (change to value: key)
        if v not in new_dict:
            new_dict[v] = k
    # if the value occurred again, remove the key with the same value
        else:
            new_dict[v] = 'rep'
    for k, v in new_dict.copy().items():
        if v == 'rep':
            del new_dict[k]

    # print(new_dict)
    # return the list of the new dict's values, which are the previous keys in the adict
    return sorted(new_dict.values())


aDict = {1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}
print(uniqueValues(aDict))
