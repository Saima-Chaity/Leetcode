# Expression Add Operators - https://leetcode.com/problems/expression-add-operators/
'''Given a string that contains only digits 0-9 and a target value, return all possibilities to add binary operators
(not unary) +, -, or * between the digits so they evaluate to the target value.

Example 1:

Input: num = "123", target = 6
Output: ["1+2+3", "1*2*3"] '''


class Solution:
    def addOperators(self, num: 'str', target: 'int') -> 'List[str]':
        output = []
        numLength = len(num)

        def addBinaryOperators(index, prevValue, currValue, expression):
            if index == numLength:
                if currValue == target:
                    output.append(expression)
                return

            for i in range(index, numLength):
                operand = num[index:i + 1]
                if len(operand) > 1 and operand[0] == "0":
                    break
                intOperand = int(operand)
                if index == 0:
                    addBinaryOperators(i + 1, intOperand, intOperand, operand)
                else:
                    addBinaryOperators(i + 1, intOperand, currValue + intOperand, expression + "+" + operand)
                    addBinaryOperators(i + 1, -intOperand, currValue - intOperand, expression + "-" + operand)
                    addBinaryOperators(i + 1, prevValue * intOperand,
                                       (currValue - prevValue) + (intOperand * prevValue), expression + "*" + operand)

        addBinaryOperators(0, 0, 0, "")
        return output
