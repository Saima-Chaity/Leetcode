# Longest Arithmetic Sequence - https://leetcode.com/problems/longest-arithmetic-sequence/
'''Given an array A of integers, return the length of the longest arithmetic subsequence in A.

Recall that a subsequence of A is a list A[i_1], A[i_2], ..., A[i_k] with 0 <= i_1 < i_2 < ... < i_k <= A.length - 1,
and that a sequence B is arithmetic if B[i+1] - B[i] are all the same value (for 0 <= i < B.length - 1).

Example 1:

Input: [3,6,9,12]
Output: 4
Explanation:
The whole array is an arithmetic sequence with steps of length = 3.
'''


class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:

        mapping = {}

        for i, a1 in enumerate(A[1:], start=1):
            for j, a2 in enumerate(A[:i]):
                difference = a1 - a2
                if (j, difference) in mapping:
                    mapping[i, difference] = mapping[j, difference] + 1
                else:
                    mapping[i, difference] = 2
        return max(mapping.values())
