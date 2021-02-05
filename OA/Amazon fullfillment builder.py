'''# Minimum Cost to Connect Sticks - https://leetcode.com/problems/minimum-cost-to-connect-sticks/
'''
import heapq
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        if len(sticks) <= 1:
            return 0

        heap = []
        for cost in sticks:
            heapq.heappush(heap, cost)

        cost = 0
        while len(heap) > 1:
            stick1 = heapq.heappop(heap)
            stick2 = heapq.heappop(heap)
            cost += stick1 + stick2
            heapq.heappush(heap, (stick1 + stick2))
        return cost