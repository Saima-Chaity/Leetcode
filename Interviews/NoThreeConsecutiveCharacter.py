'''Minimum characters that are to be inserted such that no three consecutive characters are same

Given a string str and the task is to modify the string such that no three consecutive characters are same.
In a single operation, any character can be inserted at any position in the string.
Find the minimum number of such operations required.

Examples:

Input : str = “aabbbcc”
Output: 1
“aabbdbcc” is the modified string.

Input: str = “geeksforgeeks”
Output: 0
'''

def getCount(s):
    count = 0
    i = 0
    while i < len(s) - 2:
        if s[i] == s[i + 1] and s[i] == s[i + 2]:
            count += 1
            i += 2
        else:
            i += 1
    print(count)
    return count

getCount('aabbbccc')