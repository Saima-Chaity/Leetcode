# Network Delay Time - https://leetcode.com/problems/network-delay-time/
'''There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where u is the source node, 
v is the target node, and w is the time it takes for a signal to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.

Example 1:

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2'''

# Dijkstra's Algorithm - 0(n2)
from collections import defaultdict
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        def getMinDistance(distance, seen):
            minNode = float('inf')
            minIndex = -1
            for i in range(1, N+1):
                if distance[i] < minNode and not seen[i]:
                    minNode = distance[i]
                    minIndex = i
            return minIndex
            
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        
        seen = [False] * (N+1)
        distance = {node: float('inf') for node in range(1, N+1)}
        distance[K] = 0
        
        while True:
            u = getMinDistance(distance, seen)
            if u < 0:
                break
            seen[u] = True
            for neighbour, time in graph[u]:
                if distance[neighbour] > distance[u] + time:
                    distance[neighbour] = distance[u] + time
                    
        output = max(distance.values())
        return output if output != float('inf') else -1



# Dijkstra's Algorithm - 0(nlogn)
from collections import defaultdict
import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        
        distance = {}
        q = [(0, K)]
        
        while q:
            time, node = heapq.heappop(q)
            if node in distance:
                continue
            distance[node] = time
            for neighbour, timeTravelled in graph[node]:
                if neighbour not in distance:
                    heapq.heappush(q, (time+timeTravelled, neighbour))
        return max(distance.values()) if len(distance) == N else -1