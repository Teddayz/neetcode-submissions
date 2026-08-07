import sys
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        j = len(prices) - 1
        prefix = []
        suffix = []
        smallest_prefix = sys.maxsize
        biggest_suffix = 0
        for i in range(len(prices)):
            if prices[i] < smallest_prefix:
                smallest_prefix = prices[i]
            if prices[j - i] > biggest_suffix:
                biggest_suffix = prices[j - i]
            prefix.append(smallest_prefix)
            suffix.append(biggest_suffix)
        suffix.reverse()
        for i in range(len(suffix)):
            maxProfit = max(maxProfit, suffix[i] - prefix[i])
        
        return maxProfit