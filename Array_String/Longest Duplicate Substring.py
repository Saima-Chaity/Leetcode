'''Longest Duplicate Substring - https://leetcode.com/problems/longest-duplicate-substring/

Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or
more times. The occurrences may overlap.

Return any duplicated substring that has the longest possible length. If s does not have a duplicated
substring, the answer is "".

Example 1:

Input: s = "banana"
Output: "ana"
Example 2:

Input: s = "abcd"
Output: ""
 '''

from collections import defaultdict
class Solution:
    def longestDupSubstring(self, s: str) -> str:

        def getSubstring(M):
            d = 256
            q = 2 ** 31 - 1
            h = 1
            t = 0
            mapping = defaultdict(list)
            for i in range(M - 1):
                h = (h * d) % q

            for i in range(M):
                t = (d * t + ord(s[i])) % q

            mapping[t].append(i - M + 1)
            for i in range(len(s) - M):
                t = (d * (t - ord(s[i]) * h) + ord(s[i + M])) % q
                for j in mapping[t]:
                    if s[i + 1:i + M + 1] == s[j:j + M]:
                        return (True, s[j:j + M])
                mapping[t].append(i + 1)
            return (False, "")

        left = 1
        right = len(s) - 1
        result = ""
        while left <= right:
            mid = left + (right - left) // 2
            found, candidate = getSubstring(mid)
            if found:
                left = mid + 1
                result = candidate
            else:
                right = mid - 1
        return result

