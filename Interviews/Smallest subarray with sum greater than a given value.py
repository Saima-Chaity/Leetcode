'''
Smallest subarray with sum greater than a given value
Given an array of integers and a number x, find the smallest subarray with sum greater than the given value.

Examples:
arr[] = {1, 4, 45, 6, 0, 19}
   x  =  51
Output: 3
Minimum length subarray is {4, 45, 6}

arr[] = {1, 10, 5, 2, 7}
   x  = 9
Output: 1
Minimum length subarray is {10}

arr[] = {1, 11, 100, 1, 0, 200, 3, 2, 1, 250}
    x = 280
Output: 4
Minimum length subarray is {100, 1, 0, 200}

arr[] = {1, 2, 4}
    x = 8
Output : Not Possible
Whole array sum is smaller than 8.
'''


def smallestSubWithSum(arr, n, x):

    currentSum = 0
    minLength = float('inf')
    left = 0
    right = 0
    while right < n:

        while currentSum <= x and right < n:
            currentSum += arr[right]
            right += 1

        while currentSum > x and left < n:
            minLength = min(minLength, right-left)
            currentSum -= arr[left]
            left += 1

    return minLength


# Driver program
arr1 = [1, 4, 45, 6, 10, 19]
x = 51
n1 = len(arr1)
res1 = smallestSubWithSum(arr1, n1, x)
print("Not possible") if (res1 == n1 + 1) else print(res1) # 3

arr2 = [1, 10, 5, 2, 7]
n2 = len(arr2)
x = 9
res2 = smallestSubWithSum(arr2, n2, x)
print("Not possible") if (res2 == n2 + 1) else print(res2) # 1

arr3 = [1, 11, 100, 1, 0, 200, 3, 2, 1, 250]
n3 = len(arr3)
x = 280
res3 = smallestSubWithSum(arr3, n3, x)
print("Not possible") if (res3 == n3 + 1) else print(res3) # 4