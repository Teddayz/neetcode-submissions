class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify_max(self.maxHeap)

    def addNum(self, num: int) -> None:
        if self.minHeap and num > self.minHeap[0]:
            heapq.heappush(self.minHeap, num)
            if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
                rebalance_number = heapq.heappop(self.minHeap)
                heapq.heappush_max(self.maxHeap, rebalance_number)
        else:
            heapq.heappush_max(self.maxHeap, num)
            if abs(len(self.maxHeap) - len(self.minHeap)) > 1:
                rebalance_number = heapq.heappop_max(self.maxHeap)
                heapq.heappush(self.minHeap, rebalance_number)

    def findMedian(self) -> float:
        if len(self.minHeap) == len(self.maxHeap):
            return (self.maxHeap[0] + self.minHeap[0]) / 2
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return self.maxHeap[0]
