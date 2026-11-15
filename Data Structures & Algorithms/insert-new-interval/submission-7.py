class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        # Sort the intervals based on start time
        intervals.sort(key=lambda interval: interval[0])
        res = []
        # We will go through the intervals array, and continue to add the interval to the res array as long as there is no overlap
        # between interval and the newInterval
        # Once there is an overlap, we merge the intervals and newInterval becomes the merged one.

        i = 0
        n = len(intervals)
        while i < n and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1
        
        while i < n and newInterval[1] >= intervals[i][0]:
            newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])]
            i += 1
        
        res.append(newInterval)

        while i < n:
            res.append(intervals[i])
            i += 1
        return res

