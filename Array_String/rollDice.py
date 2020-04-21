# A six-sided die is a small cube with a different number of pips on each face (side), ranging from 1 to 6.
# On any two opposite side of the cube, the number of pips adds up to 7; that is, there are three pairs of opposite sides: 1 and 6, 2 and 5, and 3 and 4.
# There are N dice lying on a table, each showing the pips on its top face. In one move, you can take one die and rotate it to an adjacent face.
# For example, you can rotate a die that shows 1 s that it shows 2, 3, 4 or 5. However, it cannot show 6 in a single move, because the faces with one pip and six pips visible are opposite sides rather than adjacent.
# You want to show the same number of pips on the top face of all N dice. Given that each of the dice can be moved multiple times, count the minimum number of moves needed to get equal faces.
#
# Write a function that, given an array A consisting of N integers describing the number of pips (from 1 to 6) shown on each die's top face, returns the minimum number of moves necessary for each die show the same number of pips.
#
# Example 1:
#
# Input: A = [1, 2, 3]
# Output: 2
# Explanation: You can pick the first two dice and rotate each of them in one move so that they all show three pips on the top face.
# Notice that you can also pick any other pair of dice in this case.
# Example 2:
#
# Input: A = [1, 1, 6]
# Output: 2
# Explanation: The only optimal answer is to rotate the last die so that it shows one pip. It is necessary to use two rotations to achieve this.

class Solution:
    def rollDice(self, nums):
        if len(nums) == 0:
            return 0

        currentMoves = 0
        minValue = float('inf')
        for i in range(1, 7):
            for num in nums:
                if num + i == 7:
                    currentMoves += 2
                elif num != i:
                    currentMoves += 1

            minValue = min(minValue, currentMoves)
            currentMoves = 0
        return minValue


print(Solution.rollDice((), [1, 2, 3]))
print(Solution.rollDice((), [1, 1, 6]))
print(Solution.rollDice((), [1, 6, 2, 3]))