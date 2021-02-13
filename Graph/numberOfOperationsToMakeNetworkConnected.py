# Number of Operations to Make Network Connected - https://leetcode.com/problems/number-of-operations-to-make-network-connected/
'''There are n computers numbered from 0 to n-1 connected by ethernet cables connections forming a network where 
connections[i] = [a, b] represents a connection between computers a and b. Any computer can reach any other computer 
directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables between two directly connected computers, 
and place them between any pair of disconnected computers to make them directly connected. Return the minimum number of 
times you need to do this in order to make all the computers connected. If it's not possible, return -1. '''

# Input: n = 4, connections = [[0,1],[0,2],[1,2]]
# Output: 1

from collections import defaultdict
import heapq

class Solution:
  def makeConnected(self, n, connections) -> int:
    if len(connections) < n - 1:
      return -1

    neighbors = defaultdict(list)
    for connection1, connection2 in connections:
      neighbors[connection1].append(connection2)
      neighbors[connection2].append(connection1)

    def dfs(node):
      if not visited[node]:
        visited[node] = 1
        for neighborComponent in neighbors[node]:
          dfs(neighborComponent)

    visited = [0] * n
    numOfOperations = 0

    for i in range(n):
      if not visited[i]:
        dfs(i)
        numOfOperations += 1
    return numOfOperations - 1


# Union find
class Solution:
    def makeConnected(self, n, connections) -> int:
        if len(connections) < n - 1:
            return -1

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

        parent = [node for node in range(n)]
        rank = [0 for i in range(n)]

        for node1, node2 in connections:
            parentOfNode1 = find(parent, node1)
            parentOfNode2 = find(parent, node2)
            if parentOfNode1 != parentOfNode2:
                union(parent, rank, parentOfNode1, parentOfNode2)

        connection = set()
        for i in range(n):
            connection.add(find(parent, i))
        return len(connection) - 1