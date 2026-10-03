"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        res = []
        intervals.sort(key=lambda x: x.start)
        for interval in intervals:
            if not res:
                res.append(interval)
                continue
            if interval.start < res[-1].end:
                return False
            res.append(interval)
        return True
