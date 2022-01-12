'''One Edit Distance - https://leetcode.com/problems/one-edit-distance/

Given two strings s and t, return true if they are both one edit distance apart, otherwise return false.

A string s is said to be one distance apart from a string t if you can:

Insert exactly one character into s to get t.
Delete exactly one character from s to get t.
Replace exactly one character of s with a different character to get t.

Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "", t = ""
Output: false
Explanation: We cannot get t from s by only one step.
'''


class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        s_length = len(s)
        t_length = len(t)
        if abs(s_length - t_length) > 1:
            return False

        i = 0
        j = 0
        while i < s_length and j < t_length and s[i] == t[j]:
            i += 1
            j += 1

        if i == s_length and j == t_length:
            return False

        if s_length > t_length:
            s = s[:i] + s[i + 1:] # deletion is only possible
            return s == t
        elif s_length < t_length:
            t = t[:j] + t[j + 1:] # insertion is only possible
            return s == t
        else: # replacing is only possible
            s = s[:i] + s[i + 1:]
            t = t[:j] + t[j + 1:]
            return s == t

# 0(1) space
class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        s_length = len(s)
        t_length = len(t)

        if abs(s_length - t_length) > 1 or s == t:
            return False

        i = 0
        j = 0
        found_unmatched = False
        while i < s_length and j < t_length:
            if s[i] != t[j]:
                if found_unmatched:
                    return False
                found_unmatched = True
                if s_length < t_length:
                    j += 1
                elif s_length > t_length:
                    i += 1
                else:
                    i += 1
                    j += 1
            else:
                i += 1
                j += 1

        return True