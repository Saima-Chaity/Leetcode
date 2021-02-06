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


'''Time complexity : O(NlogN), where NN is the length of the input array. 
Let's break it down:

Step 1) Adding N elements to the priority queue will be O(NlogN).

Step 2) We remove two of the smallest elements and then add one element to the priority queue until 
we are left with one element. Since each such operation will reduce one element from the priority 
queue, we will perform N-1 such operations. Now, we know that both add and remove operations 
take O(logN) in priority queue, therefore, complexity of this step will be O(NlogN).

Space complexity : O(N) since we will store NN elements in our priority queue.'''