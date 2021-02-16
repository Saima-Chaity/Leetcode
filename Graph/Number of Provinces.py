# Number of Provinces - https://leetcode.com/problems/number-of-provinces/
'''There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b,
and city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are
directly connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.

Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
Output: 2'''

from collections import deque
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        provinceCount = 0
        q = deque()
        visited = [False for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            if not visited[i]:
                q.append(i)
                while q:
                    node = q.popleft()
                    visited[node] = True
                    for j in range(len(isConnected)):
                        if isConnected[node][j] == 1 and not visited[j]:
                            q.append(j)
                provinceCount += 1
        return provinceCount


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

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

        n = len(isConnected)
        parent = [node for node in range(n)]
        rank = [0 for i in range(n)]

        for i in range(n):
            for j in range(i + 1, n):
                if isConnected[i][j]:
                    parentOfNode1 = find(parent, i)
                    parentOfNode2 = find(parent, j)
                    if parentOfNode1 != parentOfNode2:
                        union(parent, rank, parentOfNode1, parentOfNode2)

        connection = set()
        for i in range(n):
            connection.add(find(parent, i))
        return len(connection)