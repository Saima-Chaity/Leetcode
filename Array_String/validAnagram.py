# Valid Anagram - https://leetcode.com/problems/valid-anagram/
'''Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_count = collections.Counter(s)
        t = list(t)
        for char in t:
            if char in s_count:
                s_count[char] -= 1
                if s_count[char] == 0:
                    del s_count[char]
        if len(s_count) == 0:
            return True
        else:
            return False