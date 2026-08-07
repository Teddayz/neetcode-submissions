import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        result = []
        hash_map = {}
        for num in nums:
            hash_map[num] = hash_map.get(num, 0) + 1

        for num in nums:
            hash_map[num] += 1

        heap_list = [(-val, key) for key, val in hash_map.items()]
        heapq.heapify(heap_list)
        while (k > 0):
            result.append(heapq.heappop(heap_list)[1])
            k -= 1
        return result
