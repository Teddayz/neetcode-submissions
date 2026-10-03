class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        hashMap = {}
        
        intervals.sort(key=lambda x:x[0])
        for i in range(len(queries)):
            queries[i] = [queries[i], i]

        queries.sort(key=lambda x: x[0])

        # print(queries)            
        n = len(intervals)
        res = [-1] * len(queries)
        i = 0
        min_heap = []
        for query, index in queries:
            while i < n and intervals[i][0] <= query:
                heapq.heappush(min_heap, (intervals[i][1] - intervals[i][0] + 1, intervals[i][1]))
                i += 1
            while min_heap and min_heap[0][1] < query:
                heapq.heappop(min_heap)                    

            if min_heap:
                res[index] = min_heap[0][0]
   
        return res
