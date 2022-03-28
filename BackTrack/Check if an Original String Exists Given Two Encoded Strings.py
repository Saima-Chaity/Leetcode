'''Check if an Original String Exists Given Two Encoded Strings
https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

An original string, consisting of lowercase English letters, can be encoded by the following steps:

Arbitrarily split it into a sequence of some number of non-empty substrings.
Arbitrarily choose some elements (possibly none) of the sequence, and replace each with its length (as a numeric string).
Concatenate the sequence as the encoded string.
For example, one way to encode an original string "abcdefghijklmnop" might be:

Split it as a sequence: ["ab", "cdefghijklmn", "o", "p"].
Choose the second and third elements to be replaced by their lengths, respectively. The sequence becomes
["ab", "12", "1", "p"].
Concatenate the elements of the sequence to get the encoded string: "ab121p".
Given two encoded strings s1 and s2, consisting of lowercase English letters and digits 1-9 (inclusive), return true if
there exists an original string that could be encoded as both s1 and s2. Otherwise, return false.

Note: The test cases are generated such that the number of consecutive digits in s1 and s2 does not exceed 3.

Example 1:

Input: s1 = "internationalization", s2 = "i18n"
Output: true
Explanation: It is possible that "internationalization" was the original string.
- "internationalization"
  -> Split:       ["internationalization"]
  -> Do not replace any element
  -> Concatenate:  "internationalization", which is s1.
- "internationalization"
  -> Split:       ["i", "nternationalizatio", "n"]
  -> Replace:     ["i", "18",                 "n"]
  -> Concatenate:  "i18n", which is s2
'''

from functools import lru_cache
class Solution:
    def possiblyEquals(self, s1: str, s2: str) -> bool:

        '''
        1. both have reached end,
        2. s1 has not reached end & s1 has numeric prefix,
        3. s2 has not reached end & s2 has numeric prefix,
        4. There is no prefix lead difference between s1 & s2,
        5. s2 leads over s1,
        6. s1 leads over s2.
        '''
        return self.dfs(s1, s2, 0, 0, 0)

    @lru_cache(None)
    def dfs(self, s1, s2, i, j, diff):
        if i == len(s1) and j == len(s2):
            return diff == 0
        elif i < len(s1) and s1[i].isdigit():
            k = i
            value = 0
            while k < len(s1) and s1[k].isdigit():
                value = 10 * value + int(s1[k])
                k += 1
                if self.dfs(s1, s2, k, j, diff - value):
                    return True
        elif j < len(s2) and s2[j].isdigit():
            k = j
            value = 0
            while k < len(s2) and s2[k].isdigit():
                value = 10 * value + int(s2[k])
                k += 1
                if self.dfs(s1, s2, i, k, diff + value):
                    return True
        elif diff == 0:
            if i < len(s1) and j < len(s2) and s1[i] == s2[j] and self.dfs(s1, s2, i + 1, j + 1, diff):
                return True
        elif diff > 0:
            if i < len(s1) and self.dfs(s1, s2, i + 1, j, diff - 1):
                return True
        elif diff < 0:
            if j < len(s2) and self.dfs(s1, s2, i, j + 1, diff + 1):
                return True
        return False
