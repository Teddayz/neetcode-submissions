class Solution:
    def findMin(self, nums: list[int]) -> int:
        # Find out if left is sorted, then search in left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] <= nums[mid]:
                if nums[left] <= nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                right = mid

        return nums[left]