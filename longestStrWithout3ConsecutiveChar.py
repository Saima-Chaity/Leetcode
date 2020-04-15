'''Given A, B, C, find any string of maximum length that can be created such that no 3 consecutive characters are same.
There can be at max A 'a', B 'b' and C 'c'.'''

import  heapq
from collections import defaultdict
class Solution(object):
    def longestStr(self, A, B, C):

        heap = []
        result = ""
        temp = {}
        count = 0

        for char, freq in ('a', A), ('b', B), ('c', C):
            heapq.heappush(heap, (-freq, char))

        prevFreq = 0
        prevChar = ""
        while heap:
            freq, char = heapq.heappop(heap)
            if prevFreq != 0:
                heapq.heappush(heap, (prevFreq, prevChar))
                prevFreq = 0
                prevChar = ''
            if result[-2:] == char * 2:
                prevFreq = freq
                prevChar = char
            else:
                result += char
                freq += 1
                if freq < 0:
                    heapq.heappush(heap, (freq, char))
        return result

A, B, C = 1, 1, 6
c = Solution
print(c.longestStr((), A, B, C)) ##Output: "ccbccacc"
A, B, C = 1, 2, 3
print(c.longestStr((),A, B, C))