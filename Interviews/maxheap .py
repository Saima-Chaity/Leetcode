# Max heap
# Building Heap from Array
# Given an array of N elements. The task is to build a Binary Heap from the given array. The heap can be either Max Heap or Min Heap.

# Example:

# Input: arr[] = {4, 10, 3, 5, 1}
# Output: Corresponding Max-Heap:
#        10
#      /   \
#     5     3
#    /  \
#   4    1

# Input: arr[] = {1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17}
# Output: Corresponding Max-Heap:
#                  17
#               /      \
#             15         13
#           /    \      /  \
#          9      6    5   10
#         / \    /  \
#        4   8  3    1


class Solution:
    def heapify(arr, n ,i):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            Solution.heapify(arr, n, largest)

    def buildHeap(arr, n):
        startIndex = n // 2 - 1
        for i in range(startIndex, -1, -1):
            Solution.heapify(arr, n, i)
        
    def printHeap(arr, n): 
        print("Array representation of Heap is:"); 
    
        for i in range(n): 
            print(arr[i], end = " "); 
        print(); 

if __name__ == "__main__":
    arr = [ 1, 3, 5, 4, 6, 13, 10, 9, 8, 15, 17 ]; 
    n = len(arr)
    Solution.buildHeap(arr, n)
    Solution.printHeap(arr, n)