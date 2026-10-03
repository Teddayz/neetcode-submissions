class Solution:
    def rob(self, nums: List[int]) -> int:
        # If i rob the first house, i can only go up to the second last house
        if len(nums) == 1:
            return nums[0]
        dp1 = [0] * len(nums)
        dp1[0] = nums[0]
        dp1[1] = max(nums[0], nums[1])
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i - 2] + nums[i], dp1[i - 1])
        # If i dont rob the first house, i can go up to the last house
        dp2 = [0] * len(nums)
        dp2[0] = 0
        dp2[1] = nums[1]

        for i in range(2, len(nums)):
            dp2[i] = max(dp2[i - 2] + nums[i], dp2[i - 1])
        return max(dp1[len(nums) - 2], dp2[len(nums) - 1])