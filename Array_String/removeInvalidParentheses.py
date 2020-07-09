# Remove Invalid Parentheses - https://leetcode.com/problems/remove-invalid-parentheses/
'''Remove the minimum number of invalid parentheses in order to make the input string valid.
Return all possible results.
Note: The input string may contain letters other than the parentheses ( and ).
Input: "()())()"
Output: ["()()()", "(())()"]'''

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        # Count the number of invalid parentheses
        leftCount, rightCount = 0, 0
        for char in s:
            if char == "(":
                leftCount += 1
            elif char == ")":
                if leftCount == 0:
                    rightCount += 1
                else:
                    leftCount -= 1

        self.output = set()
        def removeInvalid(index, left, right, leftRemaining, rightRemaining, path):
            if index == len(s):
                if left == right and leftRemaining == rightRemaining == 0:
                    self.output.add(path)
            else:
                if s[index] == "(" and leftRemaining > 0:
                    removeInvalid(index + 1, left, right, leftRemaining - 1, rightRemaining, path)
                if s[index] == ")" and rightRemaining > 0:
                    removeInvalid(index + 1, left, right, leftRemaining, rightRemaining - 1, path)
                if s[index] != "(" and s[index] != ")":
                    removeInvalid(index + 1, left, right, leftRemaining, rightRemaining, path + s[index])
                elif s[index] == "(":
                    removeInvalid(index + 1, left + 1, right, leftRemaining, rightRemaining, path + "(")
                elif s[index] == ")" and left > right:
                    removeInvalid(index + 1, left, right + 1, leftRemaining, rightRemaining, path + ")")
        removeInvalid(0, 0, 0, leftCount, rightCount, "")
        return list(self.output)