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
