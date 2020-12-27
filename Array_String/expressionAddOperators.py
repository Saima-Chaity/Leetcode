# Expression Add Operators - https://leetcode.com/problems/expression-add-operators/
'''Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators
(not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] '''


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        output = []

        def backTrack(index, prevValue, currentTotal, combination):
            if index == len(num):
                if currentTotal == target:
                    output.append(combination)
                return
            for i in range(index, len(num)):
                operand = num[index:i + 1]
                if len(operand) > 1 and operand[0] == '0':  # cases for 05 which is not a valid number
                    break
                intOperand = int(operand)
                if index == 0:
                    backTrack(i + 1, intOperand, intOperand, operand)
                else:
                    backTrack(i + 1, intOperand, currentTotal + intOperand, combination + "+" + operand)
                    backTrack(i + 1, -intOperand, currentTotal - intOperand, combination + "-" + operand)
                    backTrack(i + 1, prevValue * intOperand, (currentTotal - prevValue) + (intOperand * prevValue),
                              combination + "*" + operand)

        backTrack(0, 0, 0, "0")
        return output

