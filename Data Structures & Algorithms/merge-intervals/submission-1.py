class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i = 1
        result = []
        intervals.sort()
        n = len(intervals)
        newInterval = intervals[0]
        while i < n:
            # There is overlap
            if newInterval[1] >= intervals[i][0]:
                newInterval[0] = min(newInterval[0], intervals[i][0])
                newInterval[1] = max(newInterval[1], intervals[i][1])
                if i == n - 1:
                    result.append(newInterval)
                    break
            # There is no overlap
            else:
                result.append(newInterval)
                if i == n - 1:
                    result.append(intervals[i])
                newInterval = intervals[i]
            i += 1
        if not result:
            result.append(newInterval)
        return result
            
        
