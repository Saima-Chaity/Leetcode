# Shortest Subarray with Sum at Least K - https://leetcode.com/problems/shortest-subarray-with-sum-at-least-k/
'''Return the length of the shortest, non-empty, contiguous subarray of A with sum at least K.

If there is no non-empty subarray with sum at least K, return -1.

Example 1:

Input: A = [1], K = 1
Output: 1
Example 2:

Input: A = [1,2], K = 4
Output: -1
Example 3:

Input: A = [2,-1,2], K = 3
Output: 3'''

from collections import deque
class Solution:
    def shortestSubarray(self, A: List[int], K: int) -> int:

        monotonicQueue = deque([(0, 0)]) #default value
        prefixSum = 0
        shortestLength = float('inf')
        for i in range(len(A)):
            prefixSum += A[i]
            while monotonicQueue and prefixSum < monotonicQueue[-1][1]: #Maintain a monotonic incresing sequence
                monotonicQueue.pop()
            while monotonicQueue and prefixSum - monotonicQueue[0][1] >= K: #Shrink the sliding window
                shortestLength = min(shortestLength, i + 1 - monotonicQueue.popleft()[0])
            monotonicQueue.append((i + 1, prefixSum))
        return shortestLength if shortestLength != float('inf') else -1

# Reference - https://1e9.medium.com/monotonic-queue-notes-980a019d5793