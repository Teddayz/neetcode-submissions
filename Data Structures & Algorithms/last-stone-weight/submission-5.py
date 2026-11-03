from heapq import heappush_max, heappop_max, heapify_max
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heapify_max(stones)
        while len(stones) >= 2:
            x = heappop_max(stones)
            y = heappop_max(stones)
            remaining_stone = abs(x - y)
            if remaining_stone > 0:
                heappush_max(stones, remaining_stone)
        return stones[0] if len(stones) == 1 else 0

