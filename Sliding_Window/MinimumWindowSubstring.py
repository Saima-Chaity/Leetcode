# Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/
'''Given a string S and a string T, find the minimum window in S which will contain all the characters in T in 
complexity O(n).
Example:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"'''

from collections import defaultdict, Counter
class Solution:
  def minWindow(self, s: str, t: str) -> str:
    minimumWindow = ""
    left = 0
    right = 0
    freq = defaultdict(int)
    t_freq = Counter(t)
    t_length = 0
    
    while right < len(s):
        if t_freq[s[right]] > 0:
            t_length += 1
        t_freq[s[right]] -= 1
        right += 1

        while t_length == len(t):
            if not minimumWindow or right - left < len(minimumWindow):
                minimumWindow = s[left:right]
            t_freq[s[left]] += 1
            if t_freq[s[left]] > 0:
                t_length -= 1
            left += 1
    return minimumWindow