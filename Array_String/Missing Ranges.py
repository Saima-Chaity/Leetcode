'''Missing Ranges

You are given an inclusive range [lower, upper] and a sorted unique integer array nums, where all
elements are in the inclusive range.

A number x is considered missing if x is in the range [lower, upper] and x is not in nums.

Return the smallest sorted list of ranges that cover every missing number exactly. That is, no element of nums is in
any of the ranges, and each missing number is in one of the ranges.

Each range [a,b] in the list should be output as:

"a->b" if a != b
"a" if a == b

Example 1:

Input: nums = [0,1,3,50,75], lower = 0, upper = 99
Output: ["2","4->49","51->74","76->99"]
Explanation: The ranges are:
[2,2] --> "2"
[4,49] --> "4->49"
[51,74] --> "51->74"
[76,99] --> "76->99"
Example 2:

Input: nums = [], lower = 1, upper = 1
Output: ["1"]
Explanation: The only missing range is [1,1], which becomes "1".'''


class Solution:
    def findMissingRanges(self, nums: List[int], lower: int, upper: int) -> List[str]:

        def formatRange(start, end):
            if start == end:
                return str(start)
            else:
                return str(start) + "->" + str(end)

        if not nums:
            currentRange = str(lower) + "->" + str(upper) if lower != upper else str(lower)
            return [currentRange]

        missingRange = []

        if nums[0] > lower:
            missingRange.append(formatRange(lower, nums[0] - 1))

        for i in range(1, len(nums)):
            if nums[i] - nums[i - 1] > 1:
                missingRange.append(formatRange(nums[i - 1] + 1, nums[i] - 1))

        if nums[-1] < upper:
            missingRange.append(formatRange(nums[-1] + 1, upper))
        return missingRange