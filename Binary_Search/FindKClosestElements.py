# Find K Closest Elements - https://leetcode.com/problems/find-k-closest-elements/
'''Given a sorted array arr, two integers k and x, find the k closest elements to x in the array. 
The result should also be sorted in ascending order. If there is a tie, the smaller elements are always preferred.

Example 1:

Input: arr = [1,2,3,4,5], k = 4, x = 3
Output: [1,2,3,4]
Example 2:

Input: arr = [1,2,3,4,5], k = 4, x = -1
Output: [1,2,3,4]'''

'''Complexity
Time O(log(N - K)) to binary research and find result
Space O(K) to create the returned list.'''
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        if arr[0] > x:
            return arr[:k]
        
        if arr[len(arr)-1] < x:
            return arr[-k:]
        
        low = 0
        high = len(arr)-k
        while low < high:
            mid = low + (high-low) // 2
            if x - arr[mid] > arr[mid+k] - x:
                low = mid + 1
            else:
                high = mid
        return arr[low:low+k]

# Reference -
# https://leetcode.com/problems/find-k-closest-elements/discuss/462664/Python-binary-search-with-detailed-explanation