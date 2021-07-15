'''Find N Unique Integers Sum up to Zero
Given an integer n, return any array containing n unique integers such that they add up to 0.
Example 1:

Input: n = 5
Output: [-7,-1,1,3,4]
Explanation: These arrays also are accepted [-5,-1,1,2,3] , [-3,-1,2,-2,4].
Example 2:

Input: n = 3
Output: [-1,0,1]
Example 3:

Input: n = 1
Output: [0]
'''

class Solution:
    def sumZero(self, n: int) -> List[int]:

        if n == 1:
            return [0]

        output = []

        if n % 2 != 0:
            output.append(0)

        for i in range(n // 2):
            currentNumber = i + 1
            output.append(currentNumber)
            output.append(-currentNumber)
        return output


# Another approach
def unique_sum(n: int) -> List[int]:
    if n == 1:
        return [0]

    result = []

    for i in range(n):
        result.append(i * 2 - n + 1)
    return result