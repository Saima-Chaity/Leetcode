'''Number of Ways to Stay in the Same Place After Some Steps
https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left,
1 position to the right in the array, or stay in the same place (The pointer should not be placed outside
the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after
exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
'''


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        def backTrack(index, steps):
            if index < 0 or index >= arrLen:
                return 0

            if steps == 0:
                if index == 0:
                    return 1
                return 0

            if (steps, index) in memo:
                return memo[(steps, index)]

            count = 0
            for i in [0, -1, 1]:
                count += backTrack(index + i, steps - 1)

            memo[(steps, index)] = count
            return memo[(steps, index)] % (10 ** 9 + 7)

        memo = {}
        return backTrack(0, steps)