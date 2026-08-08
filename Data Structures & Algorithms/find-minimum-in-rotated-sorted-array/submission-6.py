import sys
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minimum = sys.maxsize

        while left <= right:
            middle = (left + right) // 2
            minimum = min(minimum, nums[middle])
            if nums[middle] > nums[right]:
                left = middle + 1
            else:
                right = middle - 1
            
        return minimum