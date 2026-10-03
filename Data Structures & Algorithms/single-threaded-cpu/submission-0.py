class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        # Augment each task with its original index and sort them by their enqueue time.

        # Use a pointer to iterate through the sorted tasks and push any tasks whose enqueue time is <= current_time into a min-heap (ordered by processing_time, then index).

        # If the heap is empty, fast-forward time to the next available task's enqueue time.

        # Pop the best task from the heap, add its processing time to time, and record its index.
        res = []
        pq = []
        heapq.heapify(pq)

        for i in range(len(tasks)):
            tasks[i].append(i)
        tasks.sort(key=lambda x:x[0])

        current_time = tasks[0][0]
        pointer = 0
        while len(res) != len(tasks):
            for i in range(pointer, len(tasks)):
                if current_time >= tasks[i][0]:
                    pointer = i + 1
                    heapq.heappush(pq, (tasks[i][1], tasks[i][2]))
            if not pq:
                current_time = tasks[pointer][0]
            else:
                time, index = heapq.heappop(pq)
                res.append(index)
                current_time += time

        return res