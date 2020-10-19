# Longest Palindromic Subsequence - https://leetcode.com/problems/longest-palindromic-subsequence/
'''Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".'''

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        memo = {}
        def helper(s):
            if s in memo:
                return memo[s]
            
            if not s:
                return 0
            
            if len(s) == 1:
                return 1
            
            if s[0] == s[-1]: # first and last character are same
                output = 2 + helper(s[1:-1])
            else: # first and last character are not same, branches off into 2 paths
                output = max(helper(s[1:]), helper(s[:-1]))
            
            memo[s] = output
            return output
            
        return helper(s)