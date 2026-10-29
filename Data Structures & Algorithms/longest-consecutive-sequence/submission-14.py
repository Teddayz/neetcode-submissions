class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        res = 0
        for i in range(len(nums)):
            if nums[i] - 1 not in hashSet:
                curr = 1
                while nums[i] + curr in hashSet:
                    curr += 1
                res = max(curr, res)
        return res

            