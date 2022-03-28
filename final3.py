def isPalindrome(aString):
    '''
    aString: a string
    output: true if the string is a palindrome
    '''
    str = list(aString)
    mid = int(len(str)/2)
    for i in range(mid):
        if str[i] != str[-i-1]:
            return False
    return True


print(isPalindrome('abba'))
