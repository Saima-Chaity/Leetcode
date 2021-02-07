# Min Cost to Connect All Nodes
'''Given an undirected graph with n nodes labeled 1..n. Some of the nodes are already connected. The i-th edge connects 
nodes edges[i][0] and edges[i][1] together. Your task is to augment this set of edges with additional edges to connect 
all the nodes. Find the minimum cost to add new edges between the nodes such that all the nodes are accessible from each 
other.

Input: n = 6, edges = [[1, 4], [4, 5], [2, 3]], newEdges = [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]
Output: 7'''

from collections import defaultdict
import heapq

'''Prim's Algorithm takes O(NlgN)'''
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

    total = find(1)
    for i in range(1, n + 1):
      if find(i) != total:
        return -1
    return totalCost


'''
Time Complexity: O(ElogE) or O(ElogV). Sorting of edges takes O(ELogE) time. After sorting, we iterate
through all edges and apply find-union algorithm. The find and union operations can take atmost 
O(LogV) time. So overall complexity is O(ELogE + ELogV) time. The value of E can be atmost O(V2), 
so O(LogV) are O(LogE) same. Therefore, overall time complexity is O(ElogE) or O(ElogV)'''

#Another approach
  class Solution:
    def minimumCostToConnectNodes(self, n, edges, newEdges):

      cost_map = {}

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

      def find(city):
        if parent[city] != city:
          parent[city] = find(parent[city])
        return parent[city]

      def union(city1, city2):
        root1 = find(city1)
        root2 = find(city2)
        if root1 == root2:
          return False  # Cycle
        parent[root2] = root1  # Join roots
        return True

      # Keep track of disjoint sets. Initially each city is its own set.
      parent = {city: city for city in range(1, n + 1)}
      # Sort connections so we are always picking minimum cost edge.
      connections.sort(key=lambda x: x[2])
      totalCost = 0
      for city1, city2, cost in connections:
        if union(city1, city2):
          totalCost += cost

      # Check that all cities are connected
      root = find(n)
      for i in range(1, n + 1):
        if find(i) == root:
          continue
        else:
          return -1
      return totalCost

print(Solution.minimumCostToConnectNodes((),6, [[1, 4], [4, 5], [2, 3]], [[1, 2, 5], [1, 3, 10],
                                                                          [1, 6, 2], [5, 6, 5]])) #7
print(Solution.minimumCostToConnectNodes((),5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]],
                                         [[1, 2, 12], [3, 4, 30], [1, 5, 8]])) # 20
print(Solution.minimumCostToConnectNodes((),6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]],
                                         [[1, 6, 410], [2, 4, 800]])) # 410
print(Solution.minimumCostToConnectNodes((),6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
                         [[1, 5, 110], [2, 4, 84], [3, 4, 79]])) # 79
