# Subarray Sum Equals K - https://leetcode.com/problems/subarray-sum-equals-k/
'''Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum
equals to k.

Example 1:
Input:nums = [1,1,1], k = 2
Output: 2

Note:
The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].
'''


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        # why we are using total - k?
        # array :: 3 4 7 -2 2 1 4 2
        # presum :: 3 7 14 12 14 15 19 21
        # index :: 0 1 2 3 4 5 6 7
        # k = 7
        # Map should look like ::
        # (0,1) , (3,1), (7,1), (14,2) , (12,1) , (15,1) , (19,1) , (21,1)

        # Consider 21(presum) now what we do is sum-k that is 21-7 = 14 . Now we will check our map if we go by just count++ logic we will just increment 
        # the count once and here is where we go wrong.

        # When we search for 14 in presum array we find it on 2 and 4 index. The logic here is that 14 + 7 = 21 so the array between indexes
        # -> 3 to 7 (-2 2 1 4 2)
        # -> 5 to 7 both have sum 7 ( 1 4 2)
        # The sum is still 7 in this case because there are negative numbers that balance up for. So if we consider count++ we will have one count 
        # less as we will consider only array 5 to 7 but now we know that 14 sum occured earlier too so even that needs to be added up so map.get(sum-k).
        
        mapping = {}
        mapping[0] = 1
        total = 0
        count = 0
        for num in nums:
            total += num
            if total - k in mapping:
                count += mapping[total-k]
            if total in mapping:
                mapping[total] += 1
            else:
                mapping[total] = 1
        return count
