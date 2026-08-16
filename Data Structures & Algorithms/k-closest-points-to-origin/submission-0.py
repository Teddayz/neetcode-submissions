class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        heap = []
        heapq.heapify(heap)
        for point in points:
            distance = math.sqrt(math.pow(point[0], 2) + math.pow(point[1], 2))
            heapq.heappush(heap, (distance, point))
        while k > 0:
            node = heapq.heappop(heap)
            result.append(node[1])
            k -= 1
        return result