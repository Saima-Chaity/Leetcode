'''Custom Sorted Array

In an array, elements at any two indices can be swapped in a single operation called a move. For example,
if the array is arr = [17, 4, 8], swap arr[0] = 17 and arr[2] = 8 to get arr' = [8, 4, 17] in a single move.
Determine the minimum number of moves required to sort an array such that all of the even elements are at the
beginning of the array and all of the odd elements are at the end of the array.

Example
arr = [6, 3, 4, 5]

The following four arrays are valid custom-sorted arrays:

a = [6, 4, 3, 5]
a = [4, 6, 3, 5]
a = [6, 4, 5, 3]
a = [4, 6, 5, 3]
The most efficient sorting requires 1 move: swap the 4 and the 3.

Function Description
Complete the function moves in the editor below.

moves has the following paramenters(s):
int arr[n]: an array of positive integers

Returns
int: the minimum number of moves it takes to sort an array of integers with all even elements at earlier
indices than any odd element

Note: The order of the elements within even or odd does not matter.

Constraints

2 <= n <= 10 ^ 5
1 <= arr[i] <= 10 ^ 9, where 0 <= i < n.
It is guaranteed that array contains atleast one even and one odd element.'''

class Solution:
    def customSortedArray(self, arr):

        even = 0
        odd = len(arr)-1
        count = 0
        while even < odd:
            if arr[even] % 2 == 0:
                even += 1
                continue
            if arr[odd] % 2 != 0:
                odd -= 1
                continue

            arr[even], arr[odd] = arr[odd], arr[even]
            even += 1
            odd -= 1
            count += 1

        return count

print(Solution.customSortedArray((), [5, 7, 3, 1, 2, 4, 6, 8]))  # 4
print(Solution.customSortedArray((), [5, 7, 4, 9, 2, 3, 1]))  # 2
print(Solution.customSortedArray((), [6, 3, 4, 5]))  # 1

