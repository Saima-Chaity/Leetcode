# Subarrays with K Different Integers - https://leetcode.com/problems/subarrays-with-k-different-integers/
'''Given an array A of positive integers, call a (contiguous, not necessarily distinct) subarray of A good if
the number of different integers in that subarray is exactly K.
(For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.)
Return the number of good subarrays of A.'''

# Input: A = [1,2,1,2,3], K = 2
# Output: 7
# Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].

from collections import defaultdict
class Solution:
  def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
    def subArray(A, K):
        freq = defaultdict(int)
        left = 0
        right = 0
        output = 0

        while right < len(A):
            freq[A[right]] += 1
            while len(freq) > K:
                freq[A[left]] -= 1
                if freq[A[left]] == 0:
                    del freq[A[left]]
                left += 1
            output += right - left
            right += 1
        return output

    count = subArray(A, K) - subArray(A, K-1)
    return count