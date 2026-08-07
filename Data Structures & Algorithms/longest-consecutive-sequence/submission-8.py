class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = sorted(nums)
        left = 0
        right = left + 1
        longest = 1
        curr = 1
        while left < right and right < len(nums):
            if nums[right] == nums[left]:
                right += 1
                continue
            if nums[right] - nums[left] != 1:
                longest = max(longest, curr)
                curr = 1
                left = right
                right += 1
            else:
                curr += 1
                left = right
                right += 1
        return max(curr, longest)