class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        dp = [[None] * 2 for i in range(len(prices))]
        def traverse(index: int, canBuy: bool) -> int:
            if index >= len(prices):
                return 0 
            if dp[index][canBuy] != None:
                return dp[index][canBuy]
            if canBuy: # Means we can buy
                # Case 1: I buy
                # Case 2: I do not buy
                dp[index][canBuy] = max(-prices[index] + traverse(index + 1, False), traverse(index + 1, True))
                return dp[index][canBuy]
            else:
                # Case 4: I can sell but I need to have a cooldown
                dp[index][canBuy] = max(prices[index] + traverse(index + 2, True), traverse(index + 1, False))
                return dp[index][canBuy]

        return traverse(0, True)





        