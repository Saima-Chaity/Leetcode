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
        mapping = Counter(S)
        heap = []
        for char, freq in mapping.items():
            heapq.heappush(heap, (-freq, char))

        output = []
        while len(heap) > 1:
            freq1, char1 = heapq.heappop(heap)
            freq2, char2 = heapq.heappop(heap)
            output.extend([char1, char2])
            if abs(freq1) > 1:
                heapq.heappush(heap, (freq1+1, char1))
            if abs(freq2) > 1:
                heapq.heappush(heap, (freq2+1, char2))
        
        if len(heap) > 0:
            freq, char = heapq.heappop(heap)
            if abs(freq) > 1:
                return ""
            else:
                output.append(char)
        return "".join(output)
            
                
            