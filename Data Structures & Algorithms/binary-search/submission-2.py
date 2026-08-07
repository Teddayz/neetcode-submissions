class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # Short-circuit if nums is null
        if not nums:
            return -1
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (right + left) // 2
            if target == nums[middle]:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1