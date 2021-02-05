# Min Cost to Connect All Nodes
'''Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects 
nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect 
all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each 
other.

Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7'''

from collections import defaultdict
import heapq

#Prim's algorithm
class Solution:
  def minimumCostToConnectNodes(self, n, edges, newEdges) -> int:

    neighbors = defaultdict(list)
    addedEdges = set()

    for node1, node2, cost in newEdges:
      neighbors[node1].append((cost, node2))
      neighbors[node2].append((cost, node1))
      addedEdges.add((node1, node2))
      addedEdges.add((node2, node1))

    for node1, node2 in edges:
      if (node1, node2) not in addedEdges:
        neighbors[node1].append((0, node2))
        neighbors[node2].append((0, node1))

    q = [(0, 1)]
    visited = set()
    minCost = 0

    while q:
      cost, node = heapq.heappop(q)
      if node not in visited:
        visited.add(node)
        minCost += cost

        for cost, connectedNode in neighbors[node]:
          heapq.heappush(q, (cost, connectedNode))
    return minCost

#Kruskal's Algorithm
  def minimumCostToConnectNodes(self, n, edges, newEdges) -> int:

    memo = {}
    cost_map = {}

    def find(node):
      memo.setdefault(node, node)
      if memo[node] == node:
        return node
      else:
        return find(memo[node])

    def union(node1, node2):
      node1Value, node2Value = find(node1), find(node2)
      if node1Value != node2Value:
        memo[node1Value] = node2Value
        return nodes-1, totalCost+cost
      return nodes, totalCost


    for node1, node2, cost in newEdges:
      cost_map[(node1, node2)] = cost

    for node1, node2 in edges:
      if (node1, node2) not in cost_map:
        cost_map[(node1, node2)] = 0

    connections = []

    for key in cost_map:
      node1, node2 = key
      connections.append([node1, node2, cost_map[key]])

    if len(connections) < n - 1:
      return -1

    if n == 1:
      return 0

    connections.sort(key=lambda x: x[2])
    totalCost = 0
    nodes = n - 1

    for node1, node2, cost in connections:
      nodes, totalCost = union(node1, node2)

    return totalCost if nodes == 0 else - 1

print(Solution.minimumCostToConnectNodes((),6, [[1, 4], [4, 5], [2, 3]], [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))
print(Solution.minimumCostToConnectNodes((),5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
print(Solution.minimumCostToConnectNodes((),6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], [[1, 6, 410], [2, 4, 800]]))
print(Solution.minimumCostToConnectNodes((),6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
                         [[1, 5, 110], [2, 4, 84], [3, 4, 79]]))
