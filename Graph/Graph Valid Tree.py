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
            visited.add(node)
            for neighbour in graph[node]:
                if neighbour not in visited:
                    q.append(neighbour)
        return len(visited) == n


# DFS
from collections import defaultdict
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            for neighbour in graph[node]:
                dfs(neighbour)

        if len(edges) != n - 1:
            return False

        graph = defaultdict(set)
        for node1, node2 in edges:
            graph[node1].add(node2)
            graph[node2].add(node1)

        visited = set()
        dfs(0)
        return len(visited) == n


# Kruskal algorithm
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:

        def find(parent, node):
            if parent[node] != node:
                parent[node] = find(parent, parent[node])
            return parent[node]

        def union(parent, rank, node1, node2):
            if rank[node1] > rank[node2]:
                parent[node2] = node1
            elif rank[node1] < rank[node2]:
                parent[node1] = node2
            else:
                parent[node2] = node1
                rank[node1] += 1

        if len(edges) != n - 1:
            return False

        parent = [node for node in range(n)]
        rank = [0 for i in range(n)]

        for node1, node2 in edges:
            parentOfNode1 = find(parent, node1)
            parentOfNode2 = find(parent, node2)
            if parentOfNode1 == parentOfNode2:
                return False
            union(parent, rank, parentOfNode1, parentOfNode2)
        return True