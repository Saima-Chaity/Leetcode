# Random Pick with Weight - https://leetcode.com/problems/random-pick-with-weight/
'''You are given an array of positive integers w where w[i] describes the weight of ith index (0-indexed).

We need to call the function pickIndex() which randomly returns an integer in the range [0, w.length - 1]. pickIndex()
should return the integer proportional to its weight in the w array. For example, for w = [1, 3], the probability of
picking the index 0 is 1 / (1 + 3) = 0.25 (i.e 25%) while the probability of picking the
index 1 is 3 / (1 + 3) = 0.75 (i.e 75%).

More formally, the probability of picking index i is w[i] / sum(w).

Input
["Solution","pickIndex"]
[[[1]],[]]
Output
[null,0]

Explanation
Solution solution = new Solution([1]);
solution.pickIndex(); // return 0. Since there is only one single element on the array the only
option is to return the first element.'''

class Solution:

    def __init__(self, w: List[int]):
        self.prefixSums = []
        self.sum = 0
        prefixSum = 0
        for weight in w:
            prefixSum += weight
            self.prefixSums.append(prefixSum)
        self.sum = prefixSum

    def pickIndex(self) -> int:
        target = self.sum * random.random()
        # run a linear search to find the target zone
        for index, prefixSum in enumerate(self.prefixSums):
            if target < prefixSum:
                return index


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


#Using binary search
class Solution:

    def __init__(self, w: List[int]):
        self.prefixSums = []
        self.sum = 0
        prefixSum = 0
        for weight in w:
            prefixSum += weight
            self.prefixSums.append(prefixSum)
        self.sum = prefixSum

    def pickIndex(self) -> int:
        target = self.sum * random.random()
        low = 0
        high = len(self.prefixSums)
        while low < high:
            mid = low + (high-low) // 2
            if target > self.prefixSums[mid]:
                low = mid + 1
            else:
                high = mid
        return low

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()