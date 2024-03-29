# Maximum Units on a Truck - https://leetcode.com/problems/maximum-units-on-a-truck/
'''You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes,
where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

numberOfBoxesi is the number of boxes of type i.
numberOfUnitsPerBoxi is the number of units in each box of the type i.
You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck.
You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

Return the maximum total number of units that can be put on the truck.

Example 1:

Input: boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
Output: 8
Explanation: There are:
- 1 box of the first type that contains 3 units.
- 2 boxes of the second type that contain 2 units each.
- 3 boxes of the third type that contain 1 unit each.
You can take all the boxes of the first and second types, and one box of the third type.
The total number of units will be = (1 * 3) + (2 * 2) + (1 * 1) = 8.
Example 2:

Input: boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
Output: 91'''


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        boxTypes.sort(key=lambda x: x[1], reverse=True)
        maxUnit = 0

        for numOfBoxes, unitPerBox in boxTypes:
            able_to_load = min(truckSize, numOfBoxes)
            if able_to_load <= 0:
                break
            maxUnit += unitPerBox * able_to_load
            truckSize -= able_to_load
        return maxUnit


# Using bucket sort - 0(n) time complexity
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:

        bucket = [0] * 10001
        for numOfBoxes, unitPerBox in boxTypes:
            bucket[unitPerBox] += numOfBoxes

        boxes = []
        for i in range(len(bucket) - 1, -1, -1):
            if bucket[i]:
                boxes.append([bucket[i], i])

        total = 0
        for numOfBoxes, unitPerBox in boxes:
            ableToCarry = min(numOfBoxes, truckSize)
            if ableToCarry <= 0:
                break

            total += unitPerBox * ableToCarry
            truckSize -= ableToCarry
        return total