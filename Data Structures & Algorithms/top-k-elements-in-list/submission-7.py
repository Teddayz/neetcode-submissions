class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        result = []
        i = 0
        for (key, freq) in reversed(sorted(count.items(), key= lambda item: item[1])):
            i += 1
            result.append(key)
            if i == k:
                return result
        return []
