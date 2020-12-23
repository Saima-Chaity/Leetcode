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

    if len(p) > len(s):
      return []

    p_count = Counter(p)
    s_count = Counter()
    output = []
    for i in range(len(s)):
      s_count[s[i]] += 1
      if i >= len(p):
        s_count[s[i - len(p)]] -= 1
        if s_count[s[i - len(p)]] == 0:
          del s_count[s[i - len(p)]]
      if s_count == p_count:
        output.append(i - len(p) + 1)
    return output