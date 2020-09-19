# Distant Barcodes - https://leetcode.com/problems/distant-barcodes/
'''In a warehouse, there is a row of barcodes, where the i-th barcode is barcodes[i].
Rearrange the barcodes so that no two adjacent barcodes are equal.  You may return any answer, and it is guaranteed an answer exists.
Example 1:

Input: [1,1,1,2,2,2]
Output: [2,1,2,1,2,1]
Example 2:

Input: [1,1,1,1,2,2,3,3]
Output: [1,3,1,3,2,1,2,1]
 
Note:
1 <= barcodes.length <= 10000
1 <= barcodes[i] <= 10000'''

from collections import Counter
import heapq
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        mapping = Counter(barcodes)
        heap = []
        for code, freq in mapping.items():
            heapq.heappush(heap, (-freq, code))

        output = []
        while len(heap) > 1:
            freq1, code1 = heapq.heappop(heap)
            freq2, code2 = heapq.heappop(heap)
            output.extend([code1, code2])
            if abs(freq1) > 1:
                heapq.heappush(heap, (freq1+1, code1))
            if abs(freq2) > 1:
                heapq.heappush(heap, (freq2+1, code2))
        
        if len(heap) > 0:
            freq, code = heapq.heappop(heap)
            if abs(freq) > 1:
                return ""
            else:
                output.append(code)
        return output
            