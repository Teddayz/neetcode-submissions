class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        last = 0
        while k > 0:
            last = heapq.heappop_max(nums)
            k -= 1
        return last