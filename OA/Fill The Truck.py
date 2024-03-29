'''Fill The Truck
A Warehouse manager needs to create a shipment to fill a truck. All the products in the warehouse
are in boxes of the same size. Each product is packed in some number of units per box.

Given the number of boxes, the truck can hold, write an algorithm to determine the maximum number
of units of any mix of products that can be shipped.

Input
The input consists of five arguments:

num: an integer representing the number of products

boxes: a list of integers representing the number of available boxes for products

unitSize: an integer representing size of unitsPerBox

unitsPerBox: a list of integers representing the number of units packed in each box

truckSize: an integer representing the number of boxes the truck can carry.

Output
Return an integer representing the maximum units that can be carried by truck.

Constraints
1 <= |boxes| <= 10^5

|boxes| == |unitsPerBox|

1 <= boxes[i] <= 10^7

1 <= i <= |boxes|

1 <= unitsParBox[i] <= 10^5

1 <= j <= |unitsPerBox|

1 <= truckSize <= 10 ^ 8

Examples
Example 1:
Input:
num = 3

boxes = [1, 2, 3]

unitSize = 3

unitsPerBox = [3, 2, 1]

truckSize = 3

Output: 7
Explanation:
Product 0: because boxes[0] = 1, we know there is 1 box in product 0. And because unitsPerBox[0] = 3,
we know there is 1 box with 3 units in product 0.

Product 1: 2 boxes with 2 units each

Product 2: 3 boxes with 1 unit each

Finally, we have packed products like a list: [3, 2, 2, 1, 1, 1]

The truckSize is 3, so we pick the top 3 from the above list, which is [3, 2, 2], and return the sum 7.

The maximum number of units that can be shipped = 3 + 2 + 2 = 7 units
'''

class Solution:
    def fillTrack(self, num, boxes, unitSize, unitsPerBox, truckSize):
        boxTypes = [0] * num
        for i in range(num):
            boxTypes[i] = [boxes[i], unitsPerBox[i]]

        boxTypes.sort(key=lambda x: x[1], reverse=True)
        maxUnit = 0

        for numOfBoxes, unitPerBox in boxTypes:
            able_to_load = min(truckSize, numOfBoxes)
            if able_to_load <= 0:
                break
            maxUnit += unitPerBox * able_to_load
            truckSize -= able_to_load
        return maxUnit


num = 3
boxes = [1, 2, 3]
unitSize = 3
unitsPerBox = [3, 2, 1]
truckSize = 3
print(Solution.fillTrack((), num, boxes, unitSize, unitsPerBox, truckSize))