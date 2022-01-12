# Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/
'''Given a string, find the length of the longest substring without repeating characters.'''

# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.

from collections import OrderedDict
class Solution:
  def lengthOfLongestSubstring(self, s: str) -> int:
    if s == "":
        return 0

    freq = OrderedDict()
    maxLength = 0
    left = 0
    right = 0

    while right < len(s):
        if s[right] not in freq:
            freq[s[right]] = right
            right += 1
            maxLength = max(maxLength, right - left)
        else:
            char, lowestIndex = freq.popitem(last=False)
            left = lowestIndex + 1
    return maxLength


# Using defaultdict
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:
            return 0

        freq = defaultdict(int)
        right = 0
        left = 0
        result = 0
        while right < len(s):
            if s[right] not in freq:
                freq[s[right]] = right
                right += 1
                result = max(result, right - left)
            else:
                del freq[s[left]]
                left += 1
        return result