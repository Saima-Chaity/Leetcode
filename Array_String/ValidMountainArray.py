# Valid Mountain Array - https://leetcode.com/problems/valid-mountain-array/
'''Given an array A of integers, return true if and only if it is a valid mountain array.

Recall that A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

Example 1:

Input: [2,1]
Output: false
Example 2:

Input: [3,5,5]
Output: false
Example 3:

Input: [0,3,2,1]
Output: true'''

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        
        if len(A) < 3:
            return False
        
        isIncreasing = False
        isDecreasing = False
        
        # walk up
        i = 1
        while i < len(A):
            if A[i-1] < A[i]:
                isIncreasing = True
                i += 1
            else:
                break
        
        # walk down
        j = i
        while j < len(A):
            if A[j-1] > A[j]:
                isDecreasing = True
                j += 1
            else:
                break
        
        return True if isIncreasing and isDecreasing and j == len(A) else False

            