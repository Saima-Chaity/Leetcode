# Longest Substring with At Most K Distinct Characters - https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
'''Given a string, find the length of the longest substring T that contains at most k distinct characters.'''

# Input: s = "eceba", k = 2
# Output: 3
# Explanation: T is "ece" which its length is 3.

from collections import OrderedDict
class Solution:
  def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
    if not s or not k:
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
        if len(freq) == k+1:
            char, lowestIndex = freq.popitem(last=False)
            left = lowestIndex + 1
        maxLength = max(maxLength, right - left)
    return maxLength


#Using defaultdict
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0
        
        freq = defaultdict(int)
        left = 0
        right = 0
        result = 0
        while right < len(s):
            freq[s[right]] = freq.get(s[right], 0) + 1
            right += 1
            if len(freq) > k:
                freq[s[left]] -= 1
                if freq[s[left]] == 0:
                    del freq[s[left]]
                left += 1
            result = max(result, right-left)
        return result