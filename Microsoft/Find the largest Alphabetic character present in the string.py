'''Find the largest Alphabetic character present in the string

Given a string str, our task is to find the Largest Alphabetic Character, whose both uppercase and lowercase are
present in the string. The uppercase character should be returned. If there is no such character then return -1
otherwise print the uppercase letter of the character.

Examples:

Input: str = “admeDCAB”
Output: D
Explanation:
Both the uppercase and lowercase characters for letter D is present in the string and it is also the largest
alphabetical character, hence our output is D.

Input: str = “dAeB”
Output: -1
Explanation:
Althogh the largest character i
'''

'''Time complexity: O(n) where n is length of string. 
Space complexity: O(52)'''
def largestAlphabet(s):

    lowerLetter = [False] * 26
    upperLetter = [False] * 26

    s = list(s)
    for i in range(len(s)):
        if s[i] == s[i].lower():
            lowerLetter[ord(s[i]) - ord('a')] = True
        if s[i] == s[i].upper():
            upperLetter[ord(s[i]) - ord('A')] = True

    for i in range(len(lowerLetter)-1, -1, -1):
        if lowerLetter[i] and upperLetter[i]:
            return chr(i + ord('A'))
    return -1

print(largestAlphabet('admeDCAB'))
print(largestAlphabet('dAeB'))
print(largestAlphabet('dAeBEDbvhkjhhhDDZz'))