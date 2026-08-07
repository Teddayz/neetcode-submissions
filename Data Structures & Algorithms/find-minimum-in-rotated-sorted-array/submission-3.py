class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:
            if nums[left] < nums[right]:
                result = min(result, nums[left])
                break
            middle = (left + right) // 2
            result = min(result, nums[middle])
            if nums[left] <= nums[middle] and nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1

        return result