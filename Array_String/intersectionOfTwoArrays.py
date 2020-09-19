# Intersection of Two Arrays - https://leetcode.com/problems/intersection-of-two-arrays/
'''Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
Example 2:'''


class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:

        mapping = dict()
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        for num in nums1:
            mapping[num] = 1

        output = set()
        for num in nums2:
            if mapping:
                if num in mapping:
                    output.add(num)
                    del mapping[num]
            else:
                break
        return output


# Intersection of Two Arrays II - https://leetcode.com/problems/intersection-of-two-arrays-ii/
'''Given two arrays, write a function to compute their intersection.
Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]

Note:
Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
Follow up:
What if the given array is already sorted? How would you optimize your algorithm?
What if nums1's size is small compared to nums2's size? Which algorithm is better?
What if elements of nums2 are stored on disk, and the memory is limited such that you cannot load all elements into the memory at once?'''

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = collections.Counter(nums1)
        output = []
        for num in nums2:
            if num in count:
                output.append(num)
                count[num] -= 1
                if count[num] == 0:
                    del count[num]
        return output