'''Gray Code - https://leetcode.com/problems/gray-code/

The gray code is a binary numeral system where two successive values differ in only one bit.

Given an integer n representing the total number of bits in the code, return any sequence of gray code.

A gray code sequence must begin with 0.

Example 1:

Input: n = 2
Output: [0,1,3,2]
Explanation:
00 - 0
01 - 1
11 - 3
10 - 2
[0,2,3,1] is also a valid gray code sequence.
00 - 0
10 - 2
11 - 3
01 - 1
'''


class Solution:
    def grayCode(self, n: int) -> List[int]:

        if not n:
            return 0

        def generateGrayCode(n):
            if n == 0:
                return 0
            if n == 1:
                return [0, 1]

            result = []
            previous = generateGrayCode(n - 1)
            for i in range(len(previous) - 1, -1, -1):
                result.append(2 ** (n - 1) + previous[i])
            return previous + result

        return generateGrayCode(n)