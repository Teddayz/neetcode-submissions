class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        res = []
        intervals.sort(key=lambda interval: interval[0])
        # We can check against the res array to see if theres overlap, if there is, pop  from res and merge and append back
        for interval in intervals:
            if res and res[-1][1] >= interval[0]:
                prev_interval = res.pop()
                interval = [min(prev_interval[0], interval[0]), max(prev_interval[1], interval[1])]
            res.append(interval)
        return res