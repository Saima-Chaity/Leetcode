# Excel Sheet Column Title - https://leetcode.com/problems/excel-sheet-column-title/
'''Given a positive integer, return its corresponding column title as appear in an Excel sheet.
For example:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB
    ...
Example 1:
Input: 1
Output: "A"'''

class Solution:
    def convertToTitle(self, n: int) -> str:
        title = ''
        while n!= 0:
            n, remainder = divmod(n-1, 26)
            title += chr(remainder + ord('A'))
        return title[::-1]