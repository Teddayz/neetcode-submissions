"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        res = 1
        intervals.sort(key=lambda x:x.start)
        min_heap = []
        for interval in intervals:
            if min_heap and interval.start < min_heap[0]:
                res += 1
            else:
                if min_heap:
                    heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval.end)
        return res