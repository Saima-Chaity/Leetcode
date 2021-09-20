'''Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words,
any connected graph without simple cycles is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 edges where edges[i] = [ai, bi]
indicates that there is an undirected edge between the two nodes ai and bi in the tree, you can choose any
node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all
possible rooted trees, those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.

Example 1:
Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:'''

from collections import defaultdict, deque
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        if n <= 2:
            return [i for i in range(n)]

        neighbors = defaultdict(set)
        indegree = defaultdict(int)
        for i, j in edges:
            neighbors[i].add(j)
            neighbors[j].add(i)
            indegree[i] += 1
            indegree[j] += 1

        q = deque()
        for key, value in neighbors.items():
            if indegree[key] == 1:
                q.append(key)

        seen = len(q)
        while q:
            new_q = deque()
            for _ in range(len(q)):
                node = q.popleft()
                for neighbor in neighbors[node]:
                    indegree[node] -= 1
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 1:
                        new_q.append(neighbor)
                        seen += 1
            q = new_q
            if seen == n:
                break
        return list(q)

