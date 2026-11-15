"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""
from heapq import heappush, heappop
class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        res = 1
        # We can sort the intervals by start times but we add to a check array by earliest end time to check if theres an available room
        intervals.sort(key=lambda interval: interval.start)
        check = []
        heappush(check, intervals[0].end)
        for interval in intervals[1:]:
            # print(interval.start, interval.end)
            # print(check)
    
            if not check:
                heappush(check, interval.end)
            elif check and interval.start < check[0]:
                res += 1
                heappush(check, interval.end)
            else:
                heappop(check)
                heappush(check, interval.end)
            # print(check)
        return res
