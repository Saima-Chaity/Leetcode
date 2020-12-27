# Dot Product of Two Sparse Vectors - https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
'''Given two sparse vectors, compute their dot product.

Implement class SparseVector:

SparseVector(nums) Initializes the object with the vector nums
dotProduct(vec) Compute the dot product between the instance of SparseVector and vec
A sparse vector is a vector that has mostly zero values, you should store the sparse vector
efficiently and compute the dot product between two SparseVector.

Follow up: What if only one of the vectors is sparse?

Example 1:

Input: nums1 = [1,0,0,2,3], nums2 = [0,3,0,4,0]
Output: 8
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 1*0 + 0*3 + 0*0 + 2*4 + 3*0 = 8
Example 2:

Input: nums1 = [0,1,0,0,0], nums2 = [0,0,0,0,2]
Output: 0
Explanation: v1 = SparseVector(nums1) , v2 = SparseVector(nums2)
v1.dotProduct(v2) = 0*0 + 1*0 + 0*0 + 0*0 + 0*2 = 0'''


class SparseVector:
    def __init__(self, nums: List[int]):

        self.mapping = {}
        for index, item in enumerate(nums):
            if item != 0:
                self.mapping[index] = item

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0
        shorterMapping = self.mapping
        largerMapping = vec.mapping
        if len(self.mapping) > len(vec.mapping):
            shorterMapping = vec.mapping
            largerMapping = self.mapping

        for key1, value1 in shorterMapping.items():
            if key1 in largerMapping:
                result += value1 * largerMapping[key1]
        return result

# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)