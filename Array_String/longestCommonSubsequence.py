# Longest Common Subsequence - https://leetcode.com/problems/longest-common-subsequence/
'''Given two strings text1 and text2, return the length of their longest common subsequence.

A subsequence of a string is a new string generated from the original string with some characters(can be none) 
deleted without changing the relative order of the remaining characters. (eg, "ace" is a subsequence of "abcde" while "aec" is not). 
A common subsequence of two strings is a subsequence that is common to both strings.

If there is no common subsequence, return 0.

Example 1:

Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.
Example 2:

Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.'''

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        
        previous = [0] * (len(text1)+1)
        current = [0] * (len(text1)+1)
        
        for col in range(len(text2)):
            for row in range(len(text1)):
                if text1[row] == text2[col]:
                    current[row] = 1+previous[row-1]
                else:
                    current[row] = max(previous[row], current[row-1])
            previous, current = current, previous

        return previous[len(text1)-1]


# Reference https://www.youtube.com/watch?v=ASoaQq66foQ

# Recursion
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        memo = {}

        def findSubsequence(i, j):
            if (i, j) in memo:
                return memo[(i, j)]

            if i == len(text1) or j == len(text2):
                return 0

            if text1[i] == text2[j]:
                memo[(i, j)] = 1 + findSubsequence(i + 1, j + 1)
            else:
                memo[(i, j)] = max(findSubsequence(i, j + 1), findSubsequence(i + 1, j))

            return memo[(i, j)]

        return findSubsequence(0, 0)