class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = {}

        for i in range(len(numbers)):
            complement = target - numbers[i]
            if complement in hash_map:
                return [min(i, hash_map.get(complement)) + 1, max(i, hash_map.get(complement)) + 1]
            hash_map[numbers[i]] = i
        return []

    