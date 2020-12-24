# Reorganize String - https://leetcode.com/problems/reorganize-string/
'''Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
If possible, output any possible result.  If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"
Example 2:

Input: S = "aaab"
Output: ""

Note:
S will consist of lowercase letters and have length in range [1, 500].'''

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, S: str) -> str:

        CharCounts = Counter(S)
        heap = []
        for char, count in CharCounts.items():
            heapq.heappush(heap, (-count, char))

        result = ""
        while len(heap) > 1:
            count1, char1 = heapq.heappop(heap)
            count2, char2 = heapq.heappop(heap)
            result += char1 + char2
            if count1 != -1:
                heapq.heappush(heap, (count1 + 1, char1))
            if count2 != -1:
                heapq.heappush(heap, (count2 + 1, char2))

        if heap:
            count1, char1 = heapq.heappop(heap)
            result += char1
            if count1 != -1:
                return ""
        return result
            