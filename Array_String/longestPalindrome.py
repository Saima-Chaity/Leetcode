# Longest Palindrome - https://leetcode.com/problems/longest-palindrome/
'''Given a string s which consists of lowercase or uppercase letters, return the length of the 
longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:
Input: s = "abccccdd"
Output: 7
Explanation:
One longest palindrome that can be built is "dccaccd", whose length is 7.
Example 2:
Input: s = "bb"
Output: 2'''

class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        unpair_mapping = {}
        pairs = 0
        
        for char in s:
            if char in unpair_mapping:
                pairs += 1
                del unpair_mapping[char]
            else:
                unpair_mapping[char] = 1
        return pairs * 2 + 1 if len(unpair_mapping) != 0 else pairs * 2