'''Least Number of Unique Integers after K Removals
https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/

Given an array of integers arr and an integer k. Find the least number of unique integers after
removing exactly k elements.

Example 1:

Input: arr = [5,5,4], k = 1
Output: 1
Explanation: Remove the single 4, only 5 is left.
Example 2:
Input: arr = [4,3,1,1,3,3,2], k = 3
Output: 2
Explanation: Remove 4, 2 and either one of the two 1s or three 3s. 1 and 3 will be left.
'''

from collections import Counter
import heapq
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:

        count = Counter(arr)
        freqValues = []
        for key, value in count.items():
            heapq.heappush(freqValues, (value))

        while k:
            if freqValues[0] == 1:
                heapq.heappop(freqValues)
            else:
                freqValues[0] -= 1
            k -= 1
        return len(freqValues)



