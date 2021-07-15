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

# Another approach
def minStep(str) -> int:
        s = str
        a_count = 0
        for char in s:
            a_count += 1 if char == 'X' else 0

        b_count = len(s) - a_count
        i = 0
        j = len(s) - 1
        result = 0

        while i < j:
            while i < j and s[i] == 'X':
                i += 1
                a_count -= 1

            while i < j and s[j] == 'Y':
                j -= 1
                b_count -= 1

            if a_count and b_count:
                if a_count < b_count:
                    j -= 1
                    a_count -= 1
                    result += 1
                else:
                    i += 1
                    b_count -= 1
                    result += 1
        return result