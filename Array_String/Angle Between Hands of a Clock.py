'''Angle Between Hands of a Clock - https://leetcode.com/problems/angle-between-hands-of-a-clock/

Given two numbers, hour and minutes. Return the smaller angle (in degrees) formed between the hour and the minute hand.
Example 1:
Input: hour = 12, minutes = 30
Output: 165'''


class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        one_minute = 6
        one_hour = 30
        minute_hand = one_minute * minutes
        hour_hand = (hour % 12 + minutes / 60) * one_hour
        diff = abs(hour_hand - minute_hand)
        return min(diff, 360 - diff)