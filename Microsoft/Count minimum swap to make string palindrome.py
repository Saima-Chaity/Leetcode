'''Count minimum swap to make string palindrome

Given a string s, the task is to find out the minimum no of adjacent swaps required to make string s palindrome.
If it is not possible, then return -1.
Examples:

Input: aabcb
Output: 3
Explanation:
After 1st swap: abacb
After 2nd swap: abcab
After 3rd swap: abcba
Input: adbcdbad
Output: -1 '''


'''Time complexity is O(n2) 
Space used is O(1)
'''

from collections import Counter
def CountSwap(s, n):

    def swapChars(i, j):
        s[i], s[j] = s[j], s[i]

    def isPalindrome(s):
        oddCount = 0
        s_count = Counter(s)
        for key, value in s_count.items():
            if value % 2 != 0:
                oddCount += 1
        return oddCount <= 1

    if not isPalindrome(s):
        return -1

    left = 0
    right = n - 1
    swapCount = 0
    s = list(s)
    while left < right:
        if s[left] != s[right]:
            k = right
            while k > left and s[left] != s[k]:
                k -= 1
            if k == left:
                swapCount += 1
                swapChars(left, left+1)
            else:
                while k < right:
                    swapCount += 1
                    swapChars(k, k+1)
                    k += 1
                left += 1
                right -= 1
        elif s[left] == s[right]:
            left += 1
            right -=1
    return swapCount

s = 'aabb'
n = len(s)
ans1 = CountSwap(s, n)
ans2 = CountSwap(s[::-1], n)
print(ans1)