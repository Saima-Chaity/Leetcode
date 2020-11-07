# Two Sum III - Data structure design - https://leetcode.com/problems/two-sum-iii-data-structure-design/
'''Design and implement a TwoSum class. It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

Example 1:

add(1); add(3); add(5);
find(4) -> true
find(7) -> false'''

class TwoSum:

    def __init__(self):
        self.mapping = {}

    def add(self, number: int) -> None:
        """
        Add the number to an internal data structure..
        """
        if number not in self.mapping:
            self.mapping[number] = 1
        else:
            self.mapping[number] += 1

    def find(self, value: int) -> bool:
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        """
        for num in self.mapping.keys():
            remaining = value - num
            if remaining != num:
                if remaining in self.mapping:
                    return True
            elif self.mapping[num] > 1:
                return True
        return False

# TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


# Two Sum Less Than K - https://leetcode.com/problems/two-sum-less-than-k
'''Given an array A of integers and integer K, return the maximum S such that there exists i < j with A[i] + A[j] = S 
and S < K. If no i, j exist satisfying this equation, return -1.

Example 1:

Input: A = [34,23,1,24,75,33,54,8], K = 60
Output: 58
Explanation: 
We can use 34 and 24 to sum 58 which is less than 60.'''

class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        
        A.sort()
        i = 0
        j = len(A)-1
        maxSum = float('-inf')
        while i < j:
            sum = A[i]+A[j]
            if sum < K:
                maxSum = max(maxSum, sum)
                i += 1
            else:
                j -= 1
        return maxSum if maxSum != float('-inf') else -1


#Using Bucket sort
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:

        bucket = [0] * 1000
        for i in A:
            bucket[i - 1] += 1 # Duplicate numbers

        sortedA = []
        for index, value in enumerate(bucket):
            while value:
                sortedA.append(index + 1)
                value -= 1
        i = 0
        j = len(sortedA) - 1
        maxSum = -1
        while i < j:
            if sortedA[i] + sortedA[j] < K:
                maxSum = max(maxSum, sortedA[i] + sortedA[j])
                i += 1
            else:
                j -= 1
        return maxSum


# Two Sum IV - Input is a BST - https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
'''Given a Binary Search Tree and a target number, return true if there exist two elements in the BST such that their sum is equal to the given target.

Example 1:

Input: 
    5
   / \
  3   6
 / \   \
2   4   7

Target = 9

Output: True'''


### Queue and HashSet
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return None

        mapping = set()
        q = []
        q.append(root)

        while q:
            if q[-1] is not None:
                node = q.pop(0)
                if node is not None:
                    if (k - node.val) in mapping:
                        return True
                    mapping.add(node.val)
                    q.append(node.left)
                    q.append(node.right)
            else:
                q.pop()
        return False


###BST
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        if not root:
            return None
        output = []
        self.inorder(root, output)

        left = 0
        right = len(output) - 1
        while left < right:
            if output[left] + output[right] == k:
                return True
            elif output[left] + output[right] > k:
                right -= 1
            else:
                left += 1
        return False

    def inorder(self, node, output):
        if not node:
            return None

        self.inorder(node.left, output)
        output.append(node.val)
        self.inorder(node.right, output)


# Two Sum II - Input array is sorted - https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
'''Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a 
specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be 
less than index2.

Note:

Your returned answers (both index1 and index2) are not zero-based.
You may assume that each input would have exactly one solution and you may not use the same element twice.
Example:

Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.'''


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        mapping = {}
        for index, num in enumerate(numbers):
            remaining = target - num
            if remaining not in mapping:
                mapping[num] = index + 1
            else:
                return [index + 1, mapping[remaining]] if index + 1 < mapping[remaining] else [mapping[remaining],
                                                                                               index + 1]


# Two Sum BSTs - https://leetcode.com/problems/two-sum-bsts/
'''Given two binary search trees, return True if and only if there is a node in the first tree and a node in the second 
tree whose values sum up to a given integer target.

Example 1:

Input: root1 = [2,1,4], root2 = [1,0,3], target = 5
Output: true
Explanation: 2 and 3 sum up to 5.'''


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        if not root1 or not root2:
            return None

        stack = []
        mapping = set()
        while root1 or stack:
            while root1:
                stack.append(root1)
                root1 = root1.left
            root1 = stack.pop()
            mapping.add(target - root1.val)
            root1 = root1.right

        while root2 or stack:
            while root2:
                stack.append(root2)
                root2 = root2.left
            root2 = stack.pop()
            if root2.val in mapping:
                return True
            root2 = root2.right
        return False


# 4Sum - https://leetcode.com/problems/4sum/
'''
Given an array nums of n integers and an integer target, are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:

The solution set must not contain duplicate quadruplets.

Example:

Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        if n < 4:
            return []

        results = set()
        nums.sort()
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                threeSumResult = self.threeSum(nums[i + 1:], target - nums[i])
                for items in threeSumResult:
                    results.add(((nums[i],) + items))
        return map(list, results)

    def threeSum(self, nums, target):

        result = set()
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            newTarget = target - nums[i]
            if i == 0 or nums[i] != nums[i - 1]:
                while left < right:
                    total = nums[left] + nums[right]
                    if total < newTarget:
                        left += 1
                    elif total > newTarget:
                        right -= 1
                    else:
                        result.add((nums[i], nums[left], nums[right]))
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while left < right and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return result


# N - sum where N >= 2 solution:
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        return self.kSum(nums, target, 4)
    
    def kSum(self, nums, target, k):  
        results = []
        if len(nums) == 0 or nums[0]*k > target or nums[-1]*k < target:
            return results
        
        if k == 2:
            return self.findTwoSum(nums, target)
        
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                for path in self.kSum(nums[i+1:], target - nums[i], k-1):
                    results.append([nums[i]] + path)
        return results
    
    def findTwoSum(self, nums, target):
        results = []
        left = 0
        right = len(nums)-1
        while left < right:
            total = nums[left] + nums[right]
            if total < target:
                left += 1
            elif total > target:
                right -= 1
            else:
                results.append([nums[left], nums[right]])
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
        return results