'''Lonely Pixel I - https://leetcode.com/problems/lonely-pixel-i/

Given an m x n picture consisting of black 'B' and white 'W' pixels, return the number of black lonely pixels.

A black lonely pixel is a character 'B' that located at a specific position where the same row and same
column don't have any other black pixels.

Example 1:

Input: picture = [["W","W","B"],["W","B","W"],["B","W","W"]]
Output: 3
Explanation: All the three 'B's are black lonely pixels.
'''


class Solution:
    def findLonelyPixel(self, picture: List[List[str]]) -> int:

        count = 0
        rowCount = [0] * len(picture)
        colCount = [0] * len(picture[0])
        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B':
                    rowCount[i] += 1
                    colCount[j] += 1

        for i in range(len(picture)):
            for j in range(len(picture[0])):
                if picture[i][j] == 'B' and rowCount[i] == 1 and colCount[j] == 1:
                    count += 1
        return count