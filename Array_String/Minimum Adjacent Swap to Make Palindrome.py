'''Given a string, what is the minimum number of adjacent swaps required to
convert a string into a palindrome. If not possible, return -1.'''

from collections import Counter
def minSwapToMakePalindrome(s):

    def isPalindrome(s):
        s_count = Counter(s)
        oddCount = 0
        for char, freq in s_count.items():
            if freq % 2 != 0:
                oddCount += 1
        return oddCount <= 1

    if isPalindrome(s):
        s = list(s)
        start = 0
        end = len(s)-1
        totalSwap = 0

        while start < end:
            if s[start] == s[end]:
                start += 1
                end -= 1
            else:
                mid = end
                while mid > start and s[mid] != s[start]:
                    mid -= 1

                if mid == start:
                    s[mid], s[mid+1] = s[mid+1], s[mid]
                    totalSwap += 1
                else:
                    for i in range(mid, end):
                        s[i], s[i+1] = s[i+1], s[i]
                        totalSwap += 1
        print(totalSwap)
        return totalSwap
    else:
        return -1

print(minSwapToMakePalindrome("mamad") == 3)
print(minSwapToMakePalindrome("asflkj") == -1)
print(minSwapToMakePalindrome("aabb") == 2)
print(minSwapToMakePalindrome("ntiin") == 1)
print(minSwapToMakePalindrome('geeksfgeeks'))