class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counts = Counter(nums)
        max_heap = []
        for key, freq in counts.items():
            heapq.heappush_max(max_heap, (freq, key))
        res = []

        for i in range(k):
            freq, key = heapq.heappop_max(max_heap)
            res.append(key)
        return res