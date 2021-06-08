'''Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/

There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi]
indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city.
If a road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.

Example 1:

Input: n = 4, roads = [[0,1],[0,3],[1,2],[1,3]]
Output: 4
Explanation: The network rank of cities 0 and 1 is 4 as there are 4 roads that are connected to either 0 or 1.
The road between 0 and 1 is only counted once.
'''

'''Time complexity - 0(n^2)'''
from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(set)
        for a, b in roads:
            graph[a].add(b)
            graph[b].add(a)

        result = 0
        for i in range(n):
            for j in range(i + 1, n):
                value = (len(graph[i]) + len(graph[j])) - (i in graph[j])
                result = max(value, result)
        return result
