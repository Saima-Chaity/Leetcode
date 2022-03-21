'''Optimize Water Distribution in a Village - https://leetcode.com/problems/optimize-water-distribution-in-a-village/

There are n houses in a village. We want to supply water for all the houses by building wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i - 1] (note the -1 due to 0-indexing),
or pipe in water from another well to it. The costs to lay pipes between houses are given by the array pipes where each
pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j together using a pipe.
Connections are bidirectional, and there could be multiple valid connections between the same two houses with different
costs.

Return the minimum total cost to supply water to all houses.

Example 1:

Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so
the total cost is 3.
'''

from collections import defaultdict
import heapq
class Solution:
    def minCostToSupplyWater(self, n: int, wells: List[int], pipes: List[List[int]]) -> int:

        graph = defaultdict(list)
        for index, cost in enumerate(wells):
            graph[0].append((cost, index + 1))

        for house1, house2, cost in pipes:
            graph[house1].append((cost, house2))
            graph[house2].append((cost, house1))

        heapq.heapify(graph[0])
        heap = graph[0]
        visited = set([0])
        total_cost = 0
        while heap:
            cost, next_house = heapq.heappop(heap)
            if len(visited) == n + 1:
                return total_cost
            if next_house not in visited:
                total_cost += cost
                visited.add(next_house)
                for next_cost, neighbor in graph[next_house]:
                    if neighbor not in visited:
                        heapq.heappush(heap, (next_cost, neighbor))
        return total_cost


