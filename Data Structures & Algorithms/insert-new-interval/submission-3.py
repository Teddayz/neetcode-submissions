class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        inserted = False
        for interval in intervals:
            if interval[1] < newInterval[0]:
                result.append(interval)
            # Case 1: This interval is bigger than my newInterval but non-overlapping
            elif interval[0] > newInterval[0] and interval[0] > newInterval[1]:
                if not inserted:
                    result.append(newInterval)
                inserted = True
                result.append(interval)
            # Case 2: Overlapping
            else:
                minimum = min(newInterval[0], interval[0])
                maximum = max(newInterval[1], interval[1])
                newInterval = [minimum, maximum]
        if not inserted:
            result.append(newInterval)
        return result
