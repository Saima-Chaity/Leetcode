'''Friends Of Appropriate Ages - https://leetcode.com/problems/friends-of-appropriate-ages/

There are n persons on a social media website. You are given an integer array ages where ages[i] is the
age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

age[y] <= 0.5 * age[x] + 7
age[y] > age[x]
age[y] > 100 && age[x] < 100
Otherwise, x will send a friend request to y.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not
send a friend request to themself.

Return the total number of friend requests made.

Example 1:

Input: ages = [16,16]
Output: 2
Explanation: 2 people friend request each other.
'''


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        if not ages:
            return 0

        ages.sort()
        left = 0
        right = 0
        requestCount = 0
        for age in ages:
            while left < len(ages) and ages[left] <= 0.5 * age + 7:
                left += 1
            while right < len(ages) and ages[right] <= age:
                right += 1
            if right - 1 >= left:
                requestCount += right - left - 1
        return requestCount


# Bucket sort
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        if not ages:
            return 0

        ages_count = [0] * 121
        for age in ages:
            ages_count[age] += 1

        for i in range(1, 121):
            ages_count[i] += ages_count[i - 1]

        result = 0
        for age in ages:
            left = int(0.5 * age + 7)
            if age > left:
                result += ages_count[age] - ages_count[left] - 1
        return result
