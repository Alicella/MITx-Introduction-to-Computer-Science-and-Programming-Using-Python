# Implement a function called closest_power that meets the specifications below.

import math


def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
    # Your code here
    true_ans = math.log(num, base)
    smaller = int(true_ans)
    bigger = round(true_ans)

    lower = num - base ** smaller
    upper = base**bigger - num
    if lower <= upper:
        ans = smaller
    else:
        ans = bigger
    return ans


x = closest_power(16, 136)
print(x)
