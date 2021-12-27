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

        output = []
        s_count = Counter(s)
        for char in order:
            output.append(char * s_count[char])
            s_count[char] = 0
            del s_count[char]

        for char in s_count:
            output.append(char * s_count[char])
        return "".join(output)
