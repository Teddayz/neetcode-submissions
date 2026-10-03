class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        cleaned_intervals = []
        cleaned_intervals.append(intervals[0])
        count = 0
        for interval in intervals[1:]:
            if interval[0] < cleaned_intervals[-1][1]:
                count += 1
                continue
            else:
                cleaned_intervals.append(interval)
        # print(cleaned_intervals)
        return count
