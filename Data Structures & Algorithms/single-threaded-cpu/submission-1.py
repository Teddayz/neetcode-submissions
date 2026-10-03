class Solution:
    def getOrder(self, tasks: list[list[int]]) -> list[int]:
        res = []
        min_heap = []
        heapq.heapify(min_heap)
        n = len(tasks)
        for i in range(n):
            tasks[i].append(i)
        heapq.heapify(tasks)
        
        current_time = 0
        
        while len(res) != n:

            while tasks and current_time >= tasks[0][0]:
                task = heapq.heappop(tasks)
                heapq.heappush(min_heap, (task[1], task[2])) # Add the processing time
            # Now take the shortest processing time and add that processing time to current time
            if min_heap:
                processing_time, index = heapq.heappop(min_heap)
                current_time += processing_time
                res.append(index)
            else:
                current_time = tasks[0][0]
        return res
