# Longest Substring with At Most Two Distinct Characters - https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
'''Given a string s , find the length of the longest substring t  that contains at most 2 distinct characters.'''

# Input: "eceba"
# Output: 3
# Explanation: t is "ece" which its length is 3.

from collections import OrderedDict
class Solution:
  def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
    if s == "":
        return 0

    freq = OrderedDict()
    maxLength = 0
    left = 0
    right = 0

    while right < len(s):
        if s[right] in freq:
            del freq[s[right]]
        freq[s[right]] = right
        right += 1
        if len(freq) == 3:
            char, lowestIndex = freq.popitem(last=False)
            left = lowestIndex + 1
        maxLength = max(maxLength, right - left)
    return maxLength