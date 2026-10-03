class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        dp = [[0] * (amount + 1) for _ in range(len(coins))]
        for i in range(len(coins)):
            dp[i][0] = 1 # Amount = 0 has 1 way to solve

        for col in range(1, amount + 1):
            for row in range(len(coins) - 1, -1, -1):
                remaining_amount = amount - coins[row]
                if remaining_amount < 0: # Out of bounds
                    dp[row][col] = 0
                else:
                    if row + 1 >= len(coins):
                        dp[row][col] = 0 + dp[row][col - coins[row]]
                    else:
                        dp[row][col] = dp[row + 1][col] + dp[row][col - coins[row]]
        return dp[0][amount]
