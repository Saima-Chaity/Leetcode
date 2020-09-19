# Rearrange String k Distance Apart - https://leetcode.com/problems/rearrange-string-k-distance-apart/
'''Given a non-empty string s and an integer k, rearrange the string such that the same characters are at least distance k from each other.
All input strings are given in lowercase letters. If it is not possible to rearrange the string, return an empty string "".

Example 1:

Input: s = "aabbcc", k = 3
Output: "abcabc" 
Explanation: The same letters are at least distance 3 from each other.
Example 2:

Input: s = "aaabc", k = 3
Output: "" 
Explanation: It is not possible to rearrange the string.
Example 3:

Input: s = "aaadbbcc", k = 2
Output: "abacabcd"
Explanation: The same letters are at least distance 2 from each other.'''

from collections import Counter
import heapq
class Solution:
    def rearrangeString(self, s: str, k: int) -> str:
        if not k:
            return s
        
        mapping = Counter(s)
        heap = []
        for char, freq in mapping.items():
            heapq.heappush(heap, (-freq, char))

        output = []
        temp = []
        while len(heap) >= k:
            for i in range(k):
                freq, char = heapq.heappop(heap)
                output.append(char)
                temp.append((freq, char))

            while len(temp) > 0:
                freq, char = temp.pop()
                if abs(freq) > 1:
                    heapq.heappush(heap, (freq+1, char))

        while len(heap) > 0:
            freq, char = heapq.heappop(heap)
            if abs(freq) > 1:
                return ""
            else:
                output.append(char)
        return "".join(output)