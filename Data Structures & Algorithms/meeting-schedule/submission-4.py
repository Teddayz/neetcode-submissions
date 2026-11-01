"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        res = []
        for interval in intervals:
            if res and interval.start < res[-1].end:
                return False
            res.append(interval)

        return True