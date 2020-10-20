# Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/
'''Given a string s, find the longest palindromic substring in s. You may assume that the maximum
length of s is 1000.

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Input: "cbbd"
Output: "bb"'''


class Solution:
    def longestPalindrome(self, s: str) -> str:

        if len(s) == 1:
            return s

        p = ""

        for i in range(1, len(s)):
            p1 = self.getSubstr(i - 1, i + 1, s)
            p2 = self.getSubstr(i - 1, i, s)
            p = max([p, p1, p2], key=lambda x: len(x))
        return p

    def getSubstr(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]



# Palindromic Substrings - https://leetcode.com/problems/palindromic-substrings/
'''Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings 
even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 
Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".'''

class Solution:
    def countSubstrings(self, s: str) -> int:
        self.output = []
        for i in range(len(s)):
            p1 = self.getSubstr(i, i + 1, s)
            p2 = self.getSubstr(i, i, s)

        return len(self.output)

    def getSubstr(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            self.output.append(s[left:right+1])
            left -= 1
            right += 1

