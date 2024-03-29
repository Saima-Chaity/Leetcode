'''Earliest Time To Complete Deliveries

A geographic node has multiple Amazon buildings, each with 4 receiving docks. The number of intake
deliveries is equal to the total number of receiving docks in the node. Each intake delivery has a
predicted offloading time, and each building has a specified time when its receiving docks become
available for intake. Assuming that exactly 4 deliveries are assigned to each building and that
those deliveries run independently (asynchronously) on the receiving docks of the chosen building,
what is the earliest time that all intake deliveries can be completed?

Write an algorithm to find the earliest time that all intake deliveries can be completed.

Input
The input to the function/method consists of four arguments:

numOfBuildings: an integer representing the number of buildings;

buildingOpenTime: a list of integers representing the times at which all 4 docks of the ith building
become available;

offloadTime: a list of integers representing the offload time of each intake delivery.

Output
Return an integer representing the earliest time at which all the intake deliveries can be offloaded.

Note
The length of offloadTime is 4* numOfBuildings.

Constraints
1 <= numOfBuildings <= 10^5
1 <= buildingOpenTime[i] < 10^6
1 <= offloadTime[j] <= 10^6
0 <= i<numOfBuildings
0 <= j < 4 * numOfBuildings
Examples
Example 1:
Input:
numOfBuildings = 2

buildingOpenTime = [8, 10]

offloadTime = [2,2,3,1,8,7,4,5]

Output: 16
Explanation:
One optimal solution is as follows:

Assign the intake deliveries with the offload times 2, 3, 7, and 8 to building O that opens at time 8.

Assign the intake deliveries with the offload times 4, 2, 5, and 1 to building 1 that opens at time 10.

The first building's intake deliveries finish at times (8+2), (8+3), (8+7), and (8+8),
which are 10, 11, 15, and 16 respectively.

The second building's intake deliveries finish at times (10+4), (10+2), (10+5), and (10+1),
which are 14, 12, 15, and 11 respectively.

The maximum among those finishing times is 16. This is the earliest possible finish time.
'''

import heapq
class Solution:
    def completeDeliveries(self, numOfBuildings, buildingOpenTime, offloadTime):

        loads = []
        for time in offloadTime:
            heapq.heappush(loads, -time)

        docks = []
        for time in buildingOpenTime:
            heapq.heappush(docks, time)

        time = 0
        while docks:
            currentDock = heapq.heappop(docks)
            for i in range(4):
                time = max(time, currentDock + abs(heapq.heappop(loads)))
        return time

numOfBuildings = 2
buildingOpenTime = [8, 10]
offloadTime = [2,2,3,1,8,7,4,5]
print(Solution.completeDeliveries((), numOfBuildings, buildingOpenTime, offloadTime)) # 16