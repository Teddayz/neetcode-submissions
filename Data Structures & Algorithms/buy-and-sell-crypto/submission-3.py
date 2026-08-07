class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 0
        maxProfit = 0
        while right < len(prices):
            profit = prices[right] - prices[left]
            if profit < 0:
                left += 1
                continue
            if profit > maxProfit:
                maxProfit = profit
            right += 1
        return maxProfit
            
            