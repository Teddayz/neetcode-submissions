class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right = 0, 0
        maxCount = 0
        while right < len(nums):
            if nums[right] == 1:
                maxCount = max(maxCount, right - left + 1)
                right += 1
            else:
                count = right - left
                maxCount = max(maxCount, count)
                right += 1
                left = right
        return maxCount