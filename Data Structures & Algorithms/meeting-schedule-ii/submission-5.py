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
        pq = []
        heapq.heapify(pq) # pq will store intervals based on their interval ending time
        res = 1

        intervals.sort(key=lambda x: x.start)

        for interval in intervals:
            if not pq:
                heapq.heappush(pq, (interval.end, interval.start))
                continue
            if interval.start < pq[0][0]:
                res += 1
                heapq.heappush(pq, (interval.end, interval.start))
            else:
                heapq.heappop(pq)
                heapq.heappush(pq, (interval.end, interval.start))
        return res
            
