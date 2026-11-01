class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] * nums[i - 1]
            suffix[len(nums) - 1 - i] = suffix[len(nums) - i] * nums[len(nums) - i]
        res = [0] * len(nums)
        for i in range(len(nums)):
            res[i] = prefix[i] * suffix[i]

        return res
