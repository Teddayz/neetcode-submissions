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

        numOfRooms = 1
        index = 0
        intervals.sort(key=lambda x: x.start)
        pq = [[intervals[0].end, intervals[0].start]]
        heapq.heapify(pq)

        for interval in intervals[1:]:
            if interval.start < pq[0][0]:
                numOfRooms += 1     
            else:
                heapq.heappop(pq)
            heapq.heappush(pq, [interval.end, interval.start])

        return numOfRooms

result = [(25,579),(218,918),(623,1320),(685,1353),(1281,1307)]
intervals = intervals=[(25,579),(218,918),(1281,1307),(623,1320),(685,1353),(1308,1358)]

numOfRooms = 3
index = 2