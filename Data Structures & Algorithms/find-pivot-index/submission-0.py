class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total_sum = sum(nums)
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]
            if curr_sum == total_sum:
                return i
            total_sum -= nums[i]
        return -1