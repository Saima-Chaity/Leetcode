'''Min Deletions To Obtain String in Right Format

Given a string with only characters X and Y. Find the minimum number of characters to remove from the string such
that there is no interleaving of character X and Y and all the Xs appear before any Y.

Example 1:
Input:YXXXYXY
Output: 2
Explanation:
We can obtain XXXYY by:

Delete first Y -> XXXYXY
Delete last occurrence pf X -> XXXYY
Example 2:
Input:YYXYXX
Output: 3
Explanation:
We can remove all occurrence of X or Y:

Example 3:
Input:XXYYYY
Output: 0'''


def minStep(str) -> int:
    count = 0
    y_count = 0
    char_x = "X"
    for i in range(len(str)):
        if char_x == str[i]:
            count = min(y_count, count + 1)
        else:
            y_count += 1
    return count
