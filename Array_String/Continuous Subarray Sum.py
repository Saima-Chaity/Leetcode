# Continuous Subarray Sum - https://leetcode.com/problems/continuous-subarray-sum/
'''Given a list of non-negative numbers and a target integer k, write a function to check if the array has a
continuous subarray of size at least 2 that sums up to a multiple of k, that is, sums up to n*k where n is
also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.
Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.'''


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        '''
           /*
            ->  Idea is simple,if we want sum between index (3,5)
                we can get is using prefix concept ,means (0,5)-(0,2) means sum1-sum2
           ->   now we want (sum1-sum2)%k==0
                we can also say sum1%k-sum2%k=0
                sum1%k=sum2%k means rem1=rem2
            ->. if at jth index we are getting rem2 and it is eaual to rem1 which is at ith index
                mean we can  say sum1%k=sum2%k

                 final conclusion is that we have seen this remainder before.
            */
        '''

        mapping = {}
        mapping[0] = -1 # using -1 because for [1, 5] and k =6 at i = 1 sum will be sum % k = 0.
                        # So we need a key 0 in the map.Now i - map[sum] > 1 will return true
                        # because at this point i = 1 and map[sum] = - 1
        total = 0
        for index, num in enumerate(nums):
            total += num
            if k != 0:
                total = total % k
            if total in mapping:
                if index - mapping[total] >= 2:
                    return True
            else:
                mapping[total] = index
        return False
