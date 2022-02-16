# Permutation in String - https://leetcode.com/problems/permutation-in-string/
'''Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, 
one of the first string's permutations is the substring of the second string.

Example 1:
Input: s1 = "ab" s2 = "eidbaooo"
Output: True
Explanation: s2 contains one permutation of s1 ("ba").'''

from collections import Counter, defaultdict
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1_freq = Counter(s1)
        s2_freq = defaultdict(int)
        right = 0
        left = 0
        matchingCharCount = 0
        while right < len(s2):
            s2_freq[s2[right]] += 1
            if s2_freq[s2[right]] == s1_freq[s2[right]]:
                matchingCharCount += 1
            right += 1

            while matchingCharCount == len(s1_freq):
                if s1_freq == s2_freq:
                    return True
                s2_freq[s2[left]] -= 1
                if s2_freq[s2[left]] == 0:
                    del s2_freq[s2[left]]

                if s2[left] in s1_freq and s2_freq[s2[left]] < s1_freq[s2[left]]:
                    matchingCharCount -= 1
                left += 1
        return False

