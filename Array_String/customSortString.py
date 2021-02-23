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


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        output = []
        count = collections.Counter(T)
        for char in S:
            output.append(char * count[char])
            count[char] = 0
            if count[char] == 0:
                del count[char]

        for char in count:
            output.append(char * count[char])

        return "".join(output)
