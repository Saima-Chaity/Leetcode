from collections import defaultdict
import heapq

class Solution:
    def minCostForRepair(n, edges, edgesToRepair):
        graph = defaultdict(list)
        addedEdges = set()

        for node1, node2, cost in edgesToRepair:
            graph[node1].append((cost, node2))
            graph[node2].append((cost, node1))
            addedEdges.add((node1, node2))
            addedEdges.add((node2, node1))

        for node1, node2 in edges:
            if (node1, node2) not in addedEdges:
                graph[node1].append(((0, node2)))
                graph[node2].append((0, node1))

        q = [(0, 1)]
        visited = set()
        totalCost = 0

        while q:
            cost, node = heapq.heappop(q)
            if node not in visited:
                visited.add(node)
                totalCost += cost
                for cost, connectedNode in graph[node]:
                    if connectedNode not in visited:
                        heapq.heappush(q, (cost, connectedNode))
        return totalCost

print(Solution.minCostForRepair(6, [[1, 4], [4, 5], [2, 3]], [[1, 2, 5], [1, 3, 10], [1, 6, 2], [5, 6, 5]]))
print(Solution.minCostForRepair(5, [[1, 2], [2, 3], [3, 4], [4, 5], [1, 5]], [[1, 2, 12], [3, 4, 30], [1, 5, 8]]))
print(Solution.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [3, 5], [1, 6], [2, 4]], [[1, 6, 410], [2, 4, 800]]))
print(Solution.minCostForRepair(6, [[1, 2], [2, 3], [4, 5], [5, 6], [1, 5], [2, 4], [3, 4]],
                         [[1, 5, 110], [2, 4, 84], [3, 4, 79]]))