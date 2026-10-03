class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False
            
        target = total_sum // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always possible
        
        for num in nums:
            # Iterate backwards to avoid overwriting values needed in the same iteration
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
                
        return dp[target]