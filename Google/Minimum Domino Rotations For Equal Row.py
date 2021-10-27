'''Minimum Domino Rotations For Equal Row - https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/

In a row of dominoes, tops[i] and bottoms[i] represent the top and bottom halves of the ith domino.
(A domino is a tile with two numbers from 1 to 6 - one on each half of the tile.)

We may rotate the ith domino, so that tops[i] and bottoms[i] swap values.

Return the minimum number of rotations so that all the values in tops are the same, or all the values
in bottoms are the same.

If it cannot be done, return -1.

Example 1:

Input: tops = [2,1,2,4,2,2], bottoms = [5,2,6,2,3,2]
Output: 2
Explanation:
The first figure represents the dominoes as given by tops and bottoms: before we do any rotations.
If we rotate the second and fourth dominoes, we can make every value in the top row equal to 2, as
indicated by the second figure.
'''


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:

        def getMinimumRotation(value):
            top_rotation = bottom_rotation = 0
            for i in range(len(tops)):
                if tops[i] != value and bottoms[i] != value:
                    return -1
                if tops[i] != value:
                    top_rotation += 1
                elif bottoms[i] != value:
                    bottom_rotation += 1
            return min(top_rotation, bottom_rotation)

        rotations = getMinimumRotation(tops[0])
        if rotations != -1 or tops[0] == bottoms[0]:
            return rotations
        return getMinimumRotation(bottoms[0])