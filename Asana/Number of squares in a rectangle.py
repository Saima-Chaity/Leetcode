'''Given a m x n rectangle, how many squares are there in it?

Examples :

Input:  m = 2, n = 2
Output: 5
There are 4 squares of size 1x1 + 1 square of size 2x2.

Input: m = 4, n = 3
Output: 20
There are 12 squares of size 1x1 +
          6 squares of size 2x2 +
          2 squares of size 3x3.'''

def countSquares(m, n):
    # If n is smaller, swap m and n
    if (n < m):
        temp = m
        m = n
        n = temp

    # Now n is greater dimension,
    # apply formula
    return ((m * (m + 1) * (2 * m + 1) //
             6 + (n - m) * m * (m + 1) // 2))


# Driver Code
if __name__ == '__main__':
    m = 3
    n = 4
    print("Count of squares is "
          , countSquares(m, n))