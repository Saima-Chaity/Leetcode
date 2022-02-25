'''Cutting Ribbons - https://leetcode.com/problems/cutting-ribbons/

You are given an integer array ribbons, where ribbons[i] represents the length of the ith ribbon,
and an integer k. You may cut any of the ribbons into any number of segments of positive integer
lengths, or perform no cuts at all.

For example, if you have a ribbon of length 4, you can:
Keep the ribbon of length 4,
Cut it into one ribbon of length 3 and one ribbon of length 1,
Cut it into two ribbons of length 2,
Cut it into one ribbon of length 2 and two ribbons of length 1, or
Cut it into four ribbons of length 1.
Your goal is to obtain k ribbons of all the same positive integer length. You are allowed to throw
away any excess ribbon as a result of cutting.

Return the maximum possible positive integer length that you can obtain k ribbons of, or 0 if you
cannot obtain k ribbons of the same length.

Example 1:

Input: ribbons = [9,7,5], k = 3
Output: 5
Explanation:
- Cut the first ribbon to two ribbons, one of length 5 and one of length 4.
- Cut the second ribbon to two ribbons, one of length 5 and one of length 2.
- Keep the third ribbon as it is.
Now you have 3 ribbons of length 5.
'''

'''binary search : Time complexity: O(n*logK)'''
class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:

        if sum(ribbons) < k:
            return 0

        # Binery search is used to find the larger cut length which is mid value.
        low = 1
        high = max(ribbons)
        largestCutSoFar = 0
        while low <= high:
            mid = low + (high - low) // 2
            numberOfCut = 0
            for ribbon in ribbons:
                numberOfCut += ribbon // mid
            if numberOfCut >= k:
                largestCutSoFar = mid
                low = mid + 1
            else:
                high = mid - 1
        return largestCutSoFar

# https://leetcode.com/problems/cutting-ribbons/discuss/1623851/Reason-through-why-binary-search-works-wl-clear-explanations