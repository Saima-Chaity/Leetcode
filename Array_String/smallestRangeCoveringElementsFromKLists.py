# Smallest Range Covering Elements from K Lists - https://leetcode.com/problems/smallest-range-covering-elements-from-k-lists/
'''You have k lists of sorted integers in non-decreasing order. Find the smallest range that includes at least one number from each of the k lists.

We define the range [a, b] is smaller than range [c, d] if b - a < d - c or a < c if b - a == d - c.

Example 1:

Input: nums = [[4,10,15,24,26],[0,9,12,20],[5,18,22,30]]
Output: [20,24]
Explanation: 
List 1: [4, 10, 15, 24,26], 24 is in range [20,24].
List 2: [0, 9, 12, 20], 20 is in range [20,24].
List 3: [5, 18, 22, 30], 22 is in range [20,24].'''

import heapq
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        pq = [(row[0], index, 0) for index, row in enumerate(nums)] #Starts with value from index 0
        heapq.heapify(pq)
        result = float('-inf'), float('inf')
        maxValue = max(row[0] for row in nums) #Find max value for num in index 0
        while pq:
            minValue, i, j = heapq.heappop(pq)
            if maxValue - minValue < result[1] - result[0]:
                result = minValue, maxValue
            
            if j + 1 == len(nums[i]):
                return result
            
            nextValue = nums[i][j+1]
            maxValue = max(maxValue, nextValue)
            heapq.heappush(pq, (nextValue, i, j+1))
        
        
        
        