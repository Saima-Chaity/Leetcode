'''Confusing Number - https://leetcode.com/problems/confusing-number/

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

We can rotate digits of a number by 180 degrees to form new digits.

When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
Note that after rotating a number, we can ignore leading zeros.

For example, after rotating 8000, we have 0008 which is considered as just 8.
Given an integer n, return true if it is a confusing number, or false otherwise.

Example 1:
Input: n = 6
Output: true
Explanation: We get 9 after rotating 6, 9 is a valid number, and 9 != 6.
'''


class Solution:
    def confusingNumber(self, n: int) -> bool:

        rotatedNumbers = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        numbers = str(n)
        rotatedValue = ""
        for num in numbers:
            if num in rotatedNumbers:
                rotatedValue += rotatedNumbers[num]
            else:
                return False
        return numbers != rotatedValue[::-1]


'''Confusing Number II - https://leetcode.com/problems/confusing-number-ii/

A confusing number is a number that when rotated 180 degrees becomes a different number with each digit valid.

We can rotate digits of a number by 180 degrees to form new digits.

When 0, 1, 6, 8, and 9 are rotated 180 degrees, they become 0, 1, 9, 8, and 6 respectively.
When 2, 3, 4, 5, and 7 are rotated 180 degrees, they become invalid.
Note that after rotating a number, we can ignore leading zeros.

For example, after rotating 8000, we have 0008 which is considered as just 8.
Given an integer n, return the number of confusing numbers in the inclusive range [1, n].

Example 1:

Input: n = 20
Output: 6
Explanation: The confusing numbers are [6,9,10,16,18,19].
6 converts to 9.
9 converts to 6.
10 converts to 01 which is just 1.
16 converts to 91.
18 converts to 81.
19 converts to 61.
'''

class Solution:
    def confusingNumberII(self, n: int) -> int:

        self.result = 0

        def helper(original, rotated):
            if original != rotated:
                self.result += 1
            for num in numbers:
                if original == '0':
                    continue
                if int(original + num) > n:
                    break
                helper(original + num, rotatedNumbers[num] + rotated)

        numbers = ['0', '1', '6', '8', '9']
        rotatedNumbers = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        helper('', '')
        return self.result