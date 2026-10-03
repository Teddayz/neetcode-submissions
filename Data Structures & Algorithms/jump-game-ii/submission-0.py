class Solution:
    def jump(self, nums: List[int]) -> int:
        target = len(nums) - 1
        # numOfJumps = 0
        dp = [math.inf] * len(nums)
        dp[0] = 0
        # Since I can assume that there is always a valid answer
        # Start from the front, increment jumps by 1
        for i in range(len(nums)):
            furthest = i + nums[i]
            if furthest >= target:
                dp[target] = min(dp[i] + 1, dp[target])
            else:
                while furthest > i:
                    dp[furthest] = min(dp[i] + 1, dp[furthest])
                    furthest -= 1
        return dp[target]