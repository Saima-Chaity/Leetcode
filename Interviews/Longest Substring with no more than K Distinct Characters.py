'''Given a string str and an integer k, your task is to split str into a minimal possible number of
substrings so that there are no more than k different symbols in each of them. Return the minimal
possible number of such substrings.

eg: s = "aabeefegeeccrr" k = 3 Output = 3'''

from collections import defaultdict
class Solution:
    def possibleNumberOfSubstringWithKDistinct(self, s: str, k: int) -> int:
        if not s or not k:
            return 0

        count = 1
        hashSet = set()
        for i in range(len(s)):
            if s[i] not in hashSet and len(hashSet) == k:
                hashSet = set()
                count += 1
            hashSet.add(s[i])
        return count

print(Solution.possibleNumberOfSubstringWithKDistinct((), 'aabeefegeeccrr', 3))