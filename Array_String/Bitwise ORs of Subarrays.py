'''Bitwise ORs of Subarrays - https://leetcode.com/problems/bitwise-ors-of-subarrays/

We have an array arr of non-negative integers.

For every (contiguous) subarray sub = [arr[i], arr[i + 1], ..., arr[j]] (with i <= j), we take the bitwise OR of
all the elements in sub, obtaining a result arr[i] | arr[i + 1] | ... | arr[j].

Return the number of possible results. Results that occur more than once are only counted once in the final answer

Example 1:

Input: arr = [0]
Output: 1
Explanation: There is only one possible result: 0.
Example 2:

Input: arr = [1,1,2]
Output: 3
Explanation: The possible subarrays are [1], [1], [2], [1, 1], [1, 2], [1, 1, 2].
These yield the results 1, 1, 2, 1, 3, 3.
There are 3 unique values, so the answer is 3.
Example 3:

Input: arr = [1,2,4]
Output: 6
Explanation: The possible results are 1, 2, 3, 4, 6, and 7.
'''

class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:

        result = set(arr)
        one = set()
        one.add(arr[0])

        for i in range(1, len(arr)):
            two = set()
            for j in one:
                two.add(j | arr[i])
                result.add(j | arr[i])

            two.add(arr[i])
            one = two
        return len(result)
# Reference - https://leetcode.com/problems/bitwise-ors-of-subarrays/discuss/1240982/python-code-with-comment-might-help-to-understand-or