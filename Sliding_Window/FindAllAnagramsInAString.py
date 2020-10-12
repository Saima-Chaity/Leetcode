# Find All Anagrams in a String - https://leetcode.com/problems/find-all-anagrams-in-a-string/
'''Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.
Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.
The order of output does not matter.'''

# Input:
# s: "cbaebabacd" p: "abc"
#
# Output:
# [0, 6]

from collections import Counter
class Solution:
  def findAnagrams(self, s: str, p: str) -> List[int]:

    p_counts = Counter(p)
    s_counts = Counter()
    output = []

    if len(s) < len(p):
      return []

    for right in range(len(s)):
      s_counts[s[right]] += 1
      if right >= len(p):
        if s_counts[s[right - len(p)]] == 1:
          del s_counts[s[right - len(p)]]
        else:
          s_counts[s[right - len(p)]] -= 1

      if p_counts == s_counts:
        output.append(right - len(p) + 1)
    return output