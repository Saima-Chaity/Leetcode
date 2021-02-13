'''
Find the smallest positive integer value that cannot be represented as sum of any subset of a given array
Given a sorted array (sorted in non-decreasing order) of positive numbers, find the smallest positive integer value
that cannot be represented as sum of elements of any subset of given set.
Expected time complexity is O(n).

Examples:

Input:  arr[] = {1, 3, 6, 10, 11, 15};
Output: 2

Input:  arr[] = {1, 1, 1, 1};
Output: 5

Input:  arr[] = {1, 1, 3, 4};
Output: 10

Input:  arr[] = {1, 2, 5, 10, 20, 40};
Output: 4

Input:  arr[] = {1, 2, 3, 4, 5, 6};
Output: 22
'''


def findSmallest(arr, n):
    result = 1

    for i in range(0, n):
        if arr[i] <= result:
            result += arr[i]
        else:
            break
    return result



# Driver program to test above function
arr1 = [1, 3, 4, 5]
n1 = len(arr1)
print(findSmallest(arr1, n1)) # 2

arr2 = [1, 2, 6, 10, 11, 15]
n2 = len(arr2)
print(findSmallest(arr2, n2)) # 4

arr3 = [1, 1, 1, 1]
n3 = len(arr3)
print(findSmallest(arr3, n3)) # 5

arr4 = [1, 1, 3, 4]
n4 = len(arr4)
print(findSmallest(arr4, n4)) # 10
