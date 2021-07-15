'''Maximum even sum subsequence of length K

Given an array arr[] consisting of N positive integers, and an integer K, the task is to find the maximum
possible even sum of any subsequence of size K. If it is not possible to find any even sum subsequence
of size K, then print -1.

Examples:

Input: arr[] ={4, 2, 6, 7, 8}, K = 3
Output: 18
Explanation: Subsequence having maximum even sum of size K( = 3 ) is {4, 6, 8}.
Therefore, the required output is 4 + 6 + 8 = 18.

Input: arr[] = {5, 5, 1, 1, 3}, K = 3
Output: -1'''

'''Time Complexity: O(N * log N)
Auxiliary Space: O(N)'''

def evenSumK(arr, n, k):

    if (K > N):
        return -1

    odd_nums = []
    even_nums = []
    for i in range(n):
        if arr[i] % 2 == 0:
            even_nums.append(arr[i])
        else:
            odd_nums.append(arr[i])

    odd_nums.sort()
    even_nums.sort()
    i = len(even_nums)-1
    j = len(odd_nums)-1
    result = 0
    while k > 0:
        if k % 2 == 1:
            if i >= 0:
                result += even_nums[i]
                i -= 1
            else:
                return -1
            k -= 1
        elif i >= 1 and j >= 1:
            if even_nums[i] + even_nums[i-1] < odd_nums[j] + odd_nums[j-1]:
                result += odd_nums[j] + odd_nums[j-1]
                j -= 2
            elif even_nums[i] + even_nums[i-1] > odd_nums[j] + odd_nums[j-1]:
                result += even_nums[i] + even_nums[i-1]
                i -= 2
            k -= 2
        elif i >= 1:
            result += even_nums[i] + even_nums[i-1]
            i -= 2
            k -= 2
        elif j >= 1:
            result += odd_nums[j] + odd_nums[j-1]
            j -= 2
            k -= 2
    return result


if __name__ == '__main__':

    arr = [2, 4, 10, 3, 5]
    N = len(arr)
    K = 3

    print(evenSumK(arr, N, K))

    arr = [2, 2, 5, 1, 5, 3]
    N = len(arr)
    K = 3

    print(evenSumK(arr, N, K))