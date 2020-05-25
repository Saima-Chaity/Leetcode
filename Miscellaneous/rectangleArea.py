# Rectangle Area - https://leetcode.com/problems/rectangle-area/
'''Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45'''


class Solution:
    def computeArea(self, A: int, B: int, C: int, D: int, E: int, F: int, G: int, H: int) -> int:
        x1 = abs(A - C)
        y1 = abs(B - D)

        x2 = abs(E - G)
        y2 = abs(F - H)

        totalAreaByTwoRectangle = (x1 * y1) + (x2 * y2)

        x3 = min(C, G) - max(A, E)
        y3 = min(D, H) - max(B, F)

        if x3 <= 0 or y3 <= 0:
            return totalAreaByTwoRectangle

        overlappingArea = x3 * y3
        output = totalAreaByTwoRectangle - overlappingArea
        return output
