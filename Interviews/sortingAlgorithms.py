# Quick Sort 
# Time Complexities: Worst case O(n2), best and average Case Complexity: O(n*log n)
class Solution:
    
    def partition(arr,low,high):
        j = low
        pivot = arr[high]
        for i in range(low, high):
            if arr[i] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                j += 1
        arr[j], arr[high] = arr[high], arr[j]
        return j

    def quickSort(arr,low,high):
        if low < high:
            # pivotIndex is partitioning index, arr[pivotIndex] is now
            # at right place
            pivotIndex = Solution.partition(arr,low,high)
            # Separately sort elements before
            # partition and after partition
            Solution.quickSort(arr, low, pivotIndex-1)
            Solution.quickSort(arr, pivotIndex+1, high)
        return arr

arr = [10, 7, 8, 9, 1, 5, -1] 
n = len(arr) 
print(Solution.quickSort(arr,0,n-1))


# Merge Sort
# Time Complexities: Worst, best, average Case Complexity: O(n*log n)
class Solution:

    def merge(arr, low, mid, high):
        left = arr[low:mid+1]
        right = arr[mid+1:high+1]

        i = j = 0
        k = low #Low index
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1
        
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

        return arr
    
    def mergeSort(arr,low,high):
        if low < high:
            mid = low + (high - low) // 2
            Solution.mergeSort(arr, low, mid)
            Solution.mergeSort(arr, mid+1, high)
            Solution.merge(arr, low, mid, high)
        return arr

arr = [10, 7, 8, 9, 1, 5, -1, 3] 
n = len(arr) 
print(Solution.mergeSort(arr,0,n-1))


# Insertion Sort
# Time Complexities: Worst, average Case Complexity: O(n2), Best Case Complexity 0(n)
class Solution:
    def insert(arr):

        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j = j - 1
            arr[j+1] = key
        return arr
   
arr = [10, 7, 8, 9, 1, 5, -1, 2] 
n = len(arr) 
print(Solution.insert(arr))


# Selection Sort
# Time Complexities: Worst, best, average Case Complexity: O(n2)
class Solution:
    def selectionSort(arr):
        for i in range(0, len(arr)):
            minIndex = i
            for j in range(i+1, len(arr)):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[minIndex], arr[i] = arr[i], arr[minIndex]
        return arr

arr = [10, 7, 8, 9, 1, 5, -1, 6] 
n = len(arr) 
print(Solution.selectionSort(arr))


# Bubble Sort
# Time Complexities: Worst, average Case Complexity: O(n2), Best Case Complexity 0(n)
class Solution:
    def bubbleSort(arr):
        for i in range(0, len(arr)):
            for j in range(0, len(arr)-i-1): # Last i elements are already in place 
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

arr = [10, 7, 8, 9, 1, 5, -1, 6, -2] 
n = len(arr) 
print(Solution.bubbleSort(arr))


# Bucket Sort
# Complexity - Worst Case Complexity: O(n2), Best Case Complexity: O(n+k), Average Case Complexity: O(n)
class Solution:
    def bucketSort(arr):
        bucket = []
        for i in range(len(arr)):
            bucket.append([])

        for num in arr:
            # index_position = int(num * 10) - If we take floor numbers as input, we have to multiply it with (10 here) to get the inieger value.
            index_position = int(num / 10) # If we take integer numbers as input, we have to divide it by the interval (10 here) to get the floor value.
            bucket[index_position].append(num)

        for i in range(len(arr)):
            bucket[i] = sorted(bucket[i])
        
        k = 0
        for i in range(len(arr)):
            for j in range(len(bucket[i])):
                arr[k] = bucket[i][j]
                k += 1
        return arr

arr = [10, 7, 8, 9, 1, 5, -1, 6, -23] 
# arr = [.42, .32, .33, .52, .37, .47, .51]
n = len(arr) 
print(Solution.bucketSort(arr))