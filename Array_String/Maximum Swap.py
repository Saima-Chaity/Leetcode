# Maximum Swap - https://leetcode.com/problems/maximum-swap/
'''Given a non-negative integer, you could swap two digits at most once to get the
maximum valued number. Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.
Example 2:
Input: 9973
Output: 9973
Explanation: No swap.'''


class Solution:
    def maximumSwap(self, num: int) -> int:

        num = list(str(num))
        maxIndexSoFar = len(num) - 1
        minIndex = 0
        maxIndex = 0
        for i in range(len(num) - 1, -1, -1):  # Iterating from end to startIndex because it
                                              # tracks the largest index for duplicate maximum digit
            if num[i] > num[maxIndexSoFar]:
                maxIndexSoFar = i
            elif num[i] < num[maxIndexSoFar]:
                minIndex = i
                maxIndex = maxIndexSoFar
        num[minIndex], num[maxIndex] = num[maxIndex], num[minIndex]
        return int("".join(map(str, num)))