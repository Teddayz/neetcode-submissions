class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        intervals = []
        right = 0
        hashMap = {}
        while right < len(s):
            if s[right] in hashMap:
                hashMap[s[right]] = [hashMap[s[right]][0], right]
                right += 1
                continue
            hashMap[s[right]] = hashMap.get(s[right], [right, right])
            right += 1
        for k, interval in hashMap.items():
            intervals.append(interval)
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] < res[-1][1]:
                res[-1][0] = min(intervals[i][0], res[-1][0])
                res[-1][1] = max(intervals[i][1], res[-1][1])
            else:
                res.append(intervals[i])
        for i in range(len(res)):
            res[i] = (res[i][1] - res[i][0]) + 1

        return res