class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min = 0
        res = 0
        for i in range(1, len(prices)):
            if prices[i] < prices[min]:
                min = i
            else:
                res = max(res, prices[i] - prices[min])
        return res
