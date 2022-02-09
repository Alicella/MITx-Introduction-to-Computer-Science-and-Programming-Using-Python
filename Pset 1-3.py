# Assume s is a string of lower case characters.

# Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

# Longest substring in alphabetical order is: beggh
# In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

# Longest substring in alphabetical order is: abc

# Paste your code into this box
s = 'zyxwvutsrqponmlkjihgfedcba'

i = 0
cur_len = 0
cur_str = ''
max_len = 0
max_str = ''

while i < len(s) - 1:
    if s[i] <= s[i+1]:
        if cur_len == 0:
            # adding the current and the next character into the substring
            cur_str = s[i] + s[i+1]
            cur_len = 2
        else:
            # just need to add the next character
            cur_str += s[i+1]
            cur_len += 1

        if cur_len > max_len:
            max_len = cur_len
            max_str = cur_str

    else:
        cur_len = 0
        cur_str = ''

    i += 1

if max_len == 0:
    max_str = s[0]

print("Longest substring in alphabetical order is: " + max_str)
