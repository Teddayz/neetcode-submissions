class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0
        for num in nums:
            if num - 1 not in hashSet:
                curr = 1
                while num + curr in hashSet:
                    curr += 1
                longest = max(curr, longest)
        return longest