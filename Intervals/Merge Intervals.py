# Merge Intervals - https://leetcode.com/problems/merge-intervals/
'''Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals,
and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.'''

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        if len(intervals) == 0:
            return []
        if len(intervals) == 1:
            return intervals

        intervals.sort()
        stack = [intervals[0]]
        i = 1

        while i < len(intervals):
            if stack[-1][1] >= intervals[i][0]:
                stack[-1] = [min(stack[-1][0], intervals[i][0]), max(stack[-1][1], intervals[i][1])]
            else:
                stack.append(intervals[i])
            i += 1
        return stack


# Without sorting
class BST:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None

    def query(self, node):
        if not node:
            return []

        # merge-sort divide and conquer
        left_intervals = self.query(node.left)
        right_intervals = self.query(node.right)
        res = []

        inserted = False

        for lres in left_intervals:
            if lres[1] < node.start:
                res.append(lres)
            else:
                res.append([min(lres[0], node.start), node.end])
                inserted = True
                break

        if not inserted:
            res.append([node.start, node.end])

        for rres in right_intervals:
            if rres[0] <= node.end:
                res[-1][1] = max(node.end, rres[1])
            else:
                res.append(rres)

        return res

    def mergeInterval(self, start, end, node):
        if start >= node.end:
            if node.right:
                return self.mergeInterval(start, end, node.right)
            else:
                node.right = BST(start, end)
        elif end <= node.start:
            if node.left:
                return self.mergeInterval(start, end, node.left)
            else:
                node.left = BST(start, end)
        else:
            node.start = min(node.start, start)
            node.end = max(node.end, end)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        for i in range(len(intervals)):
            start = intervals[i][0]
            end = intervals[i][1]
            if not self.root:
                self.root = BST(start, end)
            else:
                self.mergeInterval(start, end, self.root)
        return self.query(self.root)


# https://leetcode.com/problems/merge-intervals/discuss/355318/Fully-Explained-and-Clean-Interval-Tree-for-Facebook-Follow-Up-No-Sorting

# Another approach
class BST:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.root = None
        self.output = []

    def inorder(self, node):
        if not node:
            return None
        self.inorder(node.left)
        if self.output:
            end = self.output[-1][1]
            if end >= node.start:
                i = 0
                while i < len(self.output):
                    start = self.output[i][0]
                    end = self.output[i][1]
                    if end >= node.start:
                        self.output[i] = [min(start, node.start), max(end, node.end)]
                        self.output = self.output[:i + 1]
                        break
                    i += 1
            else:
                self.output.append([node.start, node.end])
        else:
            self.output.append([node.start, node.end])
        self.inorder(node.right)

    def mergeInterval(self, start, end, node):
        if start > node.end:
            if node.right:
                return self.mergeInterval(start, end, node.right)
            else:
                node.right = BST(start, end)
        elif end < node.start:
            if node.left:
                return self.mergeInterval(start, end, node.left)
            else:
                node.left = BST(start, end)
        else:
            node.start = min(node.start, start)
            node.end = max(node.end, end)

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        for interval in intervals:
            if not self.root:
                self.root = BST(interval[0], interval[1])
            else:
                self.mergeInterval(interval[0], interval[1], self.root)

        self.inorder(self.root)
        return self.output