class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
            
        intervals.sort()
        result = [intervals[0]]
        
        for interval in intervals[1:]:
            # If the current interval overlaps with the last one in result, merge them
            if result[-1][1] >= interval[0]:
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                # Otherwise, add it as a new separate interval
                result.append(interval)
                
        return result