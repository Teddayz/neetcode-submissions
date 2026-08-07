import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_nums = list(set(nums))
        result = []
        hash_map = {}
        for num in unique_nums:
            hash_map[num] = 0

        for num in nums:
            hash_map[num] += 1

        heap_list = [(val, key) for key, val in hash_map.items()]
        heapq.heapify_max(heap_list)
        print(heap_list)
        while (k > 0):
            result.append(heapq.heappop_max(heap_list)[1])
            k -= 1
        return result
