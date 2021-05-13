'''Counts paths from a point to reach Origin

You are standing on a point (n, m) and you want to go to origin (0, 0) by taking steps either left or down i.e.
from each point you are allowed to move either in (n-1, m) or (n, m-1). Find the number of paths from point to origin.

Examples:

Input : 3 6
Output : Number of Paths 84

Input : 3 0
Output : Number of Paths 1'''

def countPaths(n, m):
    if n == 0 or m == 0:
        return 1
    return countPaths(n-1, m) + countPaths(n, m-1)

#Another approach
def countPaths(n, m):

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(0, n+1):
        for j in range(0, m+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
    return dp[n][m]


n = 3
m = 2
print(" Number of Paths ", countPaths(n, m))

n = 3
m = 6
print(" Number of Paths ", countPaths(n, m))

n = 3
m = 0
print(" Number of Paths ", countPaths(n, m))
