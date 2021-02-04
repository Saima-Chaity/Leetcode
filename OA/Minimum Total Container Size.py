'''Minimum Total Container Size
You want to move N items in k days (N >= k). You have to move at least one item per day. The items
are listed in array P, where P[i] is size of item i. You can move item i only if all items from 0
to [i - 1] are already moved. Every day you need a container to pack the item and move it. The
container size needed for day i is the maximum item size moved on that day.

Given k days and army P as the item sizes, find out the minimum total container size required to
move all the items.

Examples
Example 1:
Input: P = [10, 2, 20, 5, 15, 10, 1], d = 3
Output: 31
Explanation:
day 1 - [10, 2, 20, 5, 15]. ContainerSize = 20
day 2 - [10]. ContainerSize = 10
day 3 - [1]. ContainerSize = 1
Total = 20 + 10 + 1 = 31

Example 2:
Input: P = [10, 2, 20, 5, 15, 10, 1], d = 5
Output: 43
Explanation:
day 1 - move [10]. ContainerSize = 10
day 2 - move [2]. ContainerSize = 2
day 3 - move [20, 5, 15]. ContainerSize = 20
day 4 - move [10]. ContainerSize = 10
day 5 - move [1]. ContainerSize = 1
Total = 10 + 2 + 20 + 10 + 1 = 43

Example 3:
Input: P = [5, 4, 2, 4, 3, 4, 5, 4], d = 4
Output: 16
Explanation:
day 1 - [5, 4], containerSize = 5
day 2 - [2], containerSize = 2
day 3 - [4, 3], containerSize = 4
day 4 - [4, 5, 4], containerSize = 5
day 5 - move [1]. ContainerSize = 1
Total = 5 + 2 + 4 + 5 = 16

Example 4:
Input: P = [22, 12, 1, 14, 17], d = 2
Output: 39
Explanation:
day 1 - [22, 12], containerSize = 22
day 2 - [1, 14, 17], containerSize = 17
Total = 22 + 17 = 39

Explanation:
In order, the players achieve the ranks [4,4,3,2,1]. Since the cutOffRank is 4, all 5 players will
be able to level up their characters.

So, the output is 5.
'''

class Solution:
    def containerSize(self, product, day):

        def getMinDifficulty(index, jobDifficulty, d):
            nonlocal memo

            if d <= 0:
                return float('inf')

            if d == 1:
                if index < len(jobDifficulty):
                    return max(jobDifficulty[index:])
                return float('inf')

            if (d, index) in memo:
                return memo[(d, index)]

            minimumDifficulty = float('inf')
            for i in range(index, len(jobDifficulty)):
                minimumDifficulty = min(minimumDifficulty,
                                        getMinDifficulty(i + 1, jobDifficulty, d - 1) + max(jobDifficulty[index:i + 1]))

            memo[(d, index)] = minimumDifficulty
            return minimumDifficulty

        memo = {}
        return getMinDifficulty(0, product, day) if len(product) >= day else -1

product = [5, 4, 2, 4, 3, 4, 5, 4]
day = 4
print(Solution.containerSize((), product, day))

product = [22, 12, 1, 14, 17]
day = 2
print(Solution.containerSize((), product, day))