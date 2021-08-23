'''Longest Repeating Character Replacement - https://leetcode.com/problems/longest-repeating-character-replacement/

Given a string s that consists of only uppercase English letters, you can perform at most k operations on that string.

In one operation, you can choose any character of the string and change it to any other uppercase English character.

Find the length of the longest sub-string containing all repeating letters you can get after performing the above
operations.

Note:
Both the string's length and k will not exceed 104.

Example 1:

Input:
s = "ABAB", k = 2

Output:
4

Explanation:
Replace the two 'A's with two 'B's or vice versa.'''

from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        freq = defaultdict(int)
        left = 0
        result = 0
        i = 0
        while i < len(s):
            freq[s[i]] = freq.get(s[i], 0) + 1
            window_size = i - left + 1
            if window_size - max(freq.values()) <= k:
                result = max(result, window_size)
                i += 1
            else:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
                i += 1
        return result
