def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """

    nums_dic = {}
    for el in L:
        if el not in nums_dic:
            nums_dic[el] = 1
        else:
            nums_dic[el] += 1

    nums = sorted(nums_dic.keys(), reverse=True)
    for num in nums:
        if nums_dic[num] % 2 != 0:
            return num

    return None


print(largest_odd_times([3, 0, 5, 3, 5, 3]))
