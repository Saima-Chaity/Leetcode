'''Given 2 lists a and b. Each element is a pair of integers where the first integer represents the unique id
and the second integer represents a value. Your task is to find an element from a and an element form b such
that the sum of their values is less or equal to target and as close to target as possible. Return a list of ids
of selected elements. If no pair is possible, return an empty list.'''

# a = [[1, 2], [2, 4], [3, 6]]
# b = [[1, 2]]
# target = 7
#
# Output: [[2, 1]]
#
# Explanation:
# There are only three combinations [1, 1], [2, 1], and [3, 1], which have a total sum of 4, 6 and 8, respectively.
# Since 6 is the largest sum that does not exceed 7, [2, 1] is the optimal pair.

class Solution:
    def optimalUtilization(a, b, target):
        """
        Using 2 pointers technique to run from left of a and from right of b
        Store pairs in a dictionary, keep track closest_to_target. Return dict[closest_to_target]
        T(n): O(m + n)
        """

        if not a or not b:
            return []

        # sort by value
        a = sorted(a, key=lambda x : x[1])
        b = sorted(b, key=lambda x: x[1])

        dict = {}
        closest_to_origin = 0
        minValue = float('inf')

        # 2 pointers:
        # - i run from left -> right of a
        # - j run from right -> left of b

        i = 0
        j = len(b) - 1

        while i < len(a) and j >= 0:
            sum = a[i][1] + b[j][1]
            if sum <= target:
                if sum not in dict:
                    dict[sum] = [[a[i][0], b[j][0]]]
                else:
                    dict.get(sum).append([a[i][0], b[j][0]])

                i += 1
                if target - sum < minValue:
                    minValue = target - sum
                    closest_to_origin = sum
            else:
                j -= 1

        # sort to satisfies test cases, we can return unsorted list
        return sorted(dict[closest_to_origin], key=lambda x:x[0])


a = [[1, 3], [2, 5], [3, 7], [4, 10]]
b = [[1, 2], [2, 3], [3, 4], [4, 5]]
target = 10

print(Solution.optimalUtilization(a, b, target))