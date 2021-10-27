'''Strobogrammatic Number - https://leetcode.com/problems/strobogrammatic-number/

Given a string num which represents an integer, return true if num is a strobogrammatic number.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: num = "69"
Output: true
Example 2:

Input: num = "88"
Output: true
'''

class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        rotatedNumbers = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        result = ""
        for i in range(len(num) - 1, -1, -1):
            if num[i] not in rotatedNumbers:
                return False
            result += rotatedNumbers[num[i]]
        return result == num

# Two pointer approach
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:

        rotatedNumbers = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}

        left = 0
        right = len(num) - 1
        while left <= right:
            if num[left] not in rotatedNumbers or rotatedNumbers[num[left]] != num[right]:
                return False
            left += 1
            right -= 1
        return True


'''Strobogrammatic Number II - https://leetcode.com/problems/strobogrammatic-number-ii/

Given an integer n, return all the strobogrammatic numbers that are of length n. You may return the answer in any order.

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:

Input: n = 2
Output: ["11","69","88","96"]
Example 2:

Input: n = 1
Output: ["0","1","8"]'''


class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        rotatedNumbers = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        output = []

        def rotateHalfNumbers(number):
            result = ""
            for i in range(len(number) - 1, -1, -1):
                result += rotatedNumbers[number[i]]
            return result

        def generateNumbers(index, path):
            if index == n // 2:
                if n % 2 == 1:
                    for num in ['0', '1', '8']:
                        output.append(path + num + rotateHalfNumbers(path))
                else:
                    output.append(path + rotateHalfNumbers(path))
                return

            for key in rotatedNumbers.keys():
                if index == 0 and key == '0':
                    continue
                generateNumbers(index + 1, path + key)

        generateNumbers(0, '')
        return output

# TLE
class Solution:
    def findStrobogrammatic(self, n: int) -> List[str]:

        rotatedNumbers = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        output = []

        def generateNumbers(number):
            if len(number) == n:
                result = ""
                for i in range(len(number) - 1, -1, -1):
                    if number[i] not in rotatedNumbers:
                        break
                    result += rotatedNumbers[number[i]]
                if result == number:
                    output.append(number)
                else:
                    return

            for i in [0, 1, 6, 8, 9]:
                current_number = number + str(i)
                if len(current_number) > n:
                    break
                if number and number[0] == '0':
                    continue
                generateNumbers(number + str(i))

        generateNumbers('')
        return output