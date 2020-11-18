# Sliding Window Maximum - https://leetcode.com/problems/sliding-window-maximum/
'''You are given an array of integers nums, there is a sliding window of size k which is moving from
the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7'''

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: 'List[int]', k: 'int') -> 'List[int]':

        def cleanDeque(index):
            # remove indexes of elements not from sliding window
            if q and q[0] == index - k:
                q.popleft()

            # remove smaller elements as we need max number
            while q and nums[index] > nums[q[-1]]:
                q.pop()

        maxIndex = 0
        q = deque()
        output = []
        for i in range(k):  # first k elements
            cleanDeque(i)
            q.append(i)
            if nums[i] > nums[maxIndex]:
                maxIndex = i
        output.append(nums[maxIndex])

        for i in range(k, len(nums)):  # build output
            cleanDeque(i)
            q.append(i)
            output.append(nums[q[0]])
        return output