# Graph Valid Tree - https://leetcode.com/problems/graph-valid-tree/
'''Given n nodes labeled from 0 to n-1 and a list of undirected edges (each edge is a pair of nodes),
 write a function to check whether these edges make up a valid tree.

Example 1:

Input: n = 5, and edges = [[0,1], [0,2], [0,3], [1,4]]
Output: true
Example 2:

Input: n = 5, and edges = [[0,1], [1,2], [2,3], [1,3], [1,4]]
Output: false'''

#BFS
from collections import defaultdict, deque
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''For the graph to be a valid tree, it must have exactly n - 1 edges. Any less, and it can't possibly be fully
        connected. Any more, and it has to contain cycles. Additionally, if the graph is fully connected and contains
        exactly n - 1 edges, it can't possibly contain a cycle, and therefore must be a tree!'''

        if len(edges) != n - 1:
            return False
        graph = defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        visited = set()
        q = deque([0])
        while q:
            node = q.popleft()
            for neighbour in graph[node]:
                if neighbour not in visited:
                    q.append(neighbour)
                    visited.add(neighbour)
        return len(visited) == n


# DFS
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def isCycle(node, visited, parent):
            visited[node] = True
            for neighbour in graph[node]:
                if not visited[neighbour]:
                    if isCycle(neighbour, visited, node):
                        return True
                elif neighbour != parent:
                    return True
            return False

        if len(edges) != n - 1:
            return False

        graph = defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        visited = [False for _ in range(n)]
        if isCycle(0, visited, -1):
            return False

        for i in range(n):
            if not visited[i]:
                return False
        return True