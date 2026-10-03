class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1
        index = len(nums) - 2
        while index >= 0:
            if nums[index] + index >= goal:
                goal = index
                index -= 1
                continue
            else:
                index -= 1
        
        return goal == 0