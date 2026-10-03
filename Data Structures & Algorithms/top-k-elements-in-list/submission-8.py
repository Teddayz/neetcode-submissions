class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        max_heap = []
        heapq.heapify(max_heap)
        res = []
        for key, value in count.items():
            heapq.heappush_max(max_heap, (value, key))
        for i in range(k):
            value, key = heapq.heappop_max(max_heap)
            res.append(key)
        return res
