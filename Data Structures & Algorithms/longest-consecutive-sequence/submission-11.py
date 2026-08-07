class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in hash_set:
                curr = 1
                while num + curr in hash_set:
                    curr += 1
                longest = max(curr, longest)
        return longest