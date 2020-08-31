# Good Tuples
'''Given a list of integers, count the number of 'good tuples' that can be created.
A 'good tuple' is defined as consecutive triplets having exactly 2 duplicate elements.
Example:
nums = [4,4,6,1,2,2,2,3]
Here good tuples are: [4,4,6], [1,2,2], [2,2,3] becaue here in nums[i-1], nums[i], nums[i+1]
eaxactly 2 nubers are equal, however [2,2,2] isn't a good tuple because nums[i-1]==num[i]==nums[i+1].
Count of good tuples is 3.'''

class Solution:
    def goodTuples(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums)-1):
            if ((nums[i] == nums[i-1] and nums[i] != nums[i+1])
                or (nums[i] != nums[i-1] and nums[i] == nums[i+1])
                or (nums[i-1] == nums[i+1] and nums[i-1] != nums[i])):
                count += 1
        return count
