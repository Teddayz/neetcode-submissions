from heapq import heappush, heappop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # If I have 5 elements, I only keep k of them
        self.minHeap = []
        self.k = k
        for num in nums:
            heappush(self.minHeap, num)

        while len(self.minHeap) > k:
            heappop(self.minHeap)

    def add(self, val: int) -> int:
        heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heappop(self.minHeap)
        return self.minHeap[0]
        
