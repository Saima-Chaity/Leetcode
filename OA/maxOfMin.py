'''
Given a matrix with r rows and c columns, find the maximum score of a path starting at [0, 0] and
ending at [r-1, c-1].
The score of a path is the minimum value in that path. For example, the score of the
path 8 → 4 → 5 → 9 is 4.
Don't include the first or final entry. You can only move either down or right at any point in time.

Example 1:

Input:
[[5, 1],
 [4, 5]]

Output: 4
Explanation:
Possible paths:
5 → 1 → 5 => min value is 1
5 → 4 → 5 => min value is 4
Return the max value among minimum values => max(4, 1) = 4.
Example 2:

Input:
[[1, 2, 3]
 [4, 5, 1]]

Output: 4
Explanation:
Possible paths:
1-> 2 -> 3 -> 1
1-> 2 -> 5 -> 1
1-> 4 -> 5 -> 1
So min of all the paths = [2, 2, 4]. Note that we don't include the first and final entry.
Return the max of that, so 4.

'''


class Solution:
  # Bottom up aproach
  def maxOfMin(nums):
    rows = len(nums)
    cols = len(nums[0])

    res = [[0 for col in range(cols)] for row in range(rows)]

    for i in range(rows - 1, -1, -1):
      for j in range(cols - 1, -1, -1):
        if i == rows - 1 and j == cols - 1:
          res[i][j] = float('inf')
        elif i == rows - 1 and j != cols - 1:
          res[i][j] = min(nums[i][j], nums[i][j + 1])
        elif i != rows - 1 and j == cols - 1:
          res[i][j] = min(nums[i][j], nums[i + 1][j])
        elif i == 0 and j == 0:
          res[i][j] = max(nums[i][j + 1], nums[i + 1][j])
        else:
          res[i][j] = max(min(nums[i][j], nums[i + 1][j]), min(nums[i][j], nums[i][j + 1]))
    return res[0][0]

  # 2nd aproach
  def maxOfMin(nums):
    rows = len(nums)
    cols = len(nums[0])

    nums[0][0] = float('inf')
    nums[rows - 1][cols - 1] = float('inf')

    for i in range(1, rows):
      nums[i][0] = min(nums[i][0], nums[i - 1][0])

    for j in range(1, cols):
      nums[0][j] = min(nums[0][j], nums[0][j - 1])

    for i in range(1, rows):
      for j in range(1, cols):
        if i == rows - 1 and j == cols - 1:
          nums[i][j] = max(nums[i][j - 1], nums[i - 1][j])
        else:
          nums[i][j] = max(min(nums[i][j], nums[i - 1][j]), min(nums[i][j], nums[i][j - 1]))

    return nums[rows - 1][cols - 1]


print(Solution.maxOfMin([[5, 1], [4, 5]]))  # Output: 4
print(Solution.maxOfMin([[1, 2, 3], [4, 5, 1]]))  # Output: 4
