'''Check if a string is substring of another

Given two strings s1 and s2, find if s1 is a substring of s2. If yes, return the index of the first occurrence,
else return -1.

Examples :

Input: s1 = "for", s2 = "geeksforgeeks"
Output: 5
Explanation:
String "for" is present as a substring
of s2.

Input: s1 = "practice", s2 = "geeksforgeeks"
Output: -1.
Explanation:
There is no occurrence of "practice" in
"geeksforgeeks"'''

def substr(s, target):

    j = 0
    for i in range(len(s)):
        if j == len(target):
            break
        if s[i] == target[j]:
            j += 1
        else:
            j = 0

    if j < len(target):
        return -1
    return i - j

print(substr("GeeksForGeeks", "Fr")) # -1
print(substr("GeeksForGeeks", "For")) # 5