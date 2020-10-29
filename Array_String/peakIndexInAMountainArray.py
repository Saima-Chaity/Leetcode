# Peak Index in a Mountain Array - https://leetcode.com/problems/peak-index-in-a-mountain-array/
'''Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, return any i such that 
arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].

Example 1:

Input: arr = [0,1,0]
Output: 1
Example 2:

Input: arr = [0,2,1,0]
Output: 1'''

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        if len(arr) < 3:
            return -1
        
        peakIndex = -1
        for i in range(0, len(arr)-1):
            if i > 0 and arr[i] > arr[i-1] and arr[i] > arr[i+1]:
                peakIndex = i
        return peakIndex