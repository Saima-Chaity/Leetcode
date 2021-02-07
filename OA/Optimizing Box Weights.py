'''
Optimizing Box Weights
An Amazon fulfillment associate has a set of items that need to be packed into two boxes.
Given an interger array of the item weights to be packed, divide the item weights into two subsets,
A and B, while respecting the following rule:

the intersection of A and B is null
the union of A and B is equal to the original array
the number of elements in subsets A is minimal
the sum of A is greater than the sum of B
Return the subset A in increasing order where the sum of A's weights is greater than the sume of B's
weights. If more than one subset A exists, return the one with the maximal total weight.

Examples
Example 1:
Input:
arr = [5, 3, 2, 4, 1, 2]

Output:
4 5

Explanation:
The subset of A that satisfies the condition is [4, 5], because

A is minimal of size 2
sum(A) = 4 + 5 = 9 > sum(B) = 1 + 2 + 2 + 3 = 8
the intersection of A and B is null and their union is equal to arr
the subset A with the maximal sum is [4, 5]
'''

from collections import Counter
import heapq

def optimizing_box_weights(arr: [int]) -> [int]:
    # WRITE YOUR BRILLIANT CODE HERE

    totalSum = sum(arr)
    heap = []
    for index, num in enumerate(arr):
        heapq.heappush(heap, (-num, index))

    a = []
    b = []
    sumOfA = 0
    removedIndex = []
    while heap and sumOfA < totalSum:
        num, index = heapq.heappop(heap)
        num = abs(num)
        totalSum -= num
        a.append(num)
        sumOfA += num
        removedIndex.append(index)

    for i in range(len(arr)):
        if i not in removedIndex:
            b.append(arr[i])

    isUnion = False
    isIntersection = False
    mapping = Counter(b)
    for item in a:
        if item in mapping:
            isIntersection = True
            break

    newArr = a + b
    if Counter(newArr) == Counter(arr):
        isUnion = True

    return a if isUnion and not isIntersection else []

print(optimizing_box_weights([1, 2, 5, 8, 3])) #[5, 8]
print(optimizing_box_weights([10, 5, 3, 1, 20])) #[20]
print(optimizing_box_weights([5, 3, 2, 4, 1, 2])) #[4, 5]