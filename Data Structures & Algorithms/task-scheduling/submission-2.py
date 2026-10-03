class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashMap = {}
        heap = []
        time = 0
        count = Counter(tasks)
        heap = [-cnt for cnt in count.values()]

        heapq.heapify(heap)
        queue = deque()

        while heap or queue:
            time += 1
            if heap:
                freq = heapq.heappop(heap) + 1
                if freq < 0:
                    queue.append((freq, n + time))
            if queue and queue[0][1] == time:
                heapq.heappush(heap, queue.popleft()[0])
        
        return time