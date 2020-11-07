# Non-overlapping Intervals - https://leetcode.com/problems/non-overlapping-intervals/
'''Given a collection of intervals, find the minimum number of intervals you need to remove to make the 
rest of the intervals non-overlapping.

Example 1:

Input: [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
Example 2:

Input: [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.'''

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Case 1:
        # The two intervals currently considered are non-overlapping:   
        # Case 2:
        # The two intervals currently considered are overlapping and the end point of 
        # the later interval falls before the end point of the previous interval  
        # Case 3:
        # The two intervals currently considered are overlapping and the end point of 
        # the later interval falls after the end point of the previous interval
            
        if not intervals:
            return 0
        
        intervals.sort(key = lambda x:x[0])
        prev_end = intervals[0][1]
        count = 0
        for start, end in intervals[1:]:
            if start < prev_end:
                if prev_end > end:
                    prev_end = end
                count += 1
            else:
                prev_end = end
        return count
        
        