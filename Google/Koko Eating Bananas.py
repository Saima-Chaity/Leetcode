'''Koko Eating Bananas - https://leetcode.com/problems/koko-eating-bananas/

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k
bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any
more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
'''


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        '''We have to find the minimum Banana eating speed per hour.
            Bounds will be
            1 <= bound <= highest element in the array
            use Binary search
            low -> 1, high -> getHigh(piles) -> yields the highest element in the array.
            find mid
            find if koko can eat all the bananas in the given hours with the speed of mid.
            divide every element in the array with mid and if the element is odd add 1 and divide.
            count the hours taken total.
            return true if it is lower than h.
            If "yes"
            then find if she can lower her speed because we have to find the minimum (Banana Eating speed per hour).
            high = mid - 1
            If "No"
            then the current speed is insufficient for her and we should increase the eating speed.
            low = mid + 1
        '''
        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            time_use = 0
            for p in piles:
                time_use += math.ceil(p / mid)
            if time_use <= h:
                right = mid
            else:
                left = mid + 1
        return left




