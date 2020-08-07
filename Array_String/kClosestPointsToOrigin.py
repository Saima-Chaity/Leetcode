# K Closest Points to Origin - https://leetcode.com/problems/k-closest-points-to-origin/
'''We have a list of points on the plane.  Find the K closest points to the origin (0, 0).
(Here, the distance between two points on a plane is the Euclidean distance.)
You may return the answer in any order.  The answer is guaranteed to be unique
(except for the order that it is in.)

Input: points = [[1,3],[-2,2]], K = 1
Output: [[-2,2]]
Explanation:
The distance between (1, 3) and the origin is sqrt(10).
The distance between (-2, 2) and the origin is sqrt(8).
Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
We only want the closest K = 1 points from the origin, so the answer is just [[-2,2]].'''

# Using heap
import heapq
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        heap = []
        for point in points:
            totalValue = point[0] * point[0] + point[1] * point[1]
            heapq.heappush(heap, (totalValue, point))
        return [heapq.heappop(heap)[1] for _ in range(K)]


# Quickselect
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        self.findKthCloset(0, len(points) - 1, K, points)
        return points[:K]

    def calculateSqrt(self, point):
        return point[0] * point[0] + point[1] * point[1]

    def findKthCloset(self, left, right, k, points):
        if left >= right:
            return

        pivotIndex = random.randint(left, right)
        pivotIndex = self.partition(points, left, right, pivotIndex)

        if k < pivotIndex:
            self.findKthCloset(left, pivotIndex - 1, k, points)
        elif k > pivotIndex:
            self.findKthCloset(pivotIndex + 1, right, k, points)

    def partition(self, points, left, right, pivotIndex):
        pivotValue = self.calculateSqrt(points[pivotIndex])
        points[right], points[pivotIndex] = points[pivotIndex], points[right]
        low = left
        for i in range(left, right):
            if self.calculateSqrt(points[i]) < pivotValue:
                points[low], points[i] = points[i], points[low]
                low += 1
        points[right], points[low] = points[low], points[right]
        return low


