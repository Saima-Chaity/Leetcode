# Custom Sort String - https://leetcode.com/problems/custom-sort-string/
'''S and T are strings composed of lowercase letters. In S, no letter occurs more than once.

S was sorted in some custom order previously. We want to permute the characters of T so that they match the order
that S was sorted. More specifically, if x occurs before y in S, then x should occur before y in the returned string.

Return any permutation of T (as a string) that satisfies this property.

Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"'''

from collections import Counter
class Solution:
    def customSortString(self, order: str, s: str) -> str:

        s_count = Counter(s)
        result = ""
        for char in order:
            if char in s_count:
                result += char * s_count[char]
                del s_count[char]

        for char, freq in s_count.items():
            result += char * freq
        return result