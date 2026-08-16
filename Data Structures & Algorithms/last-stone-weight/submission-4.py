class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if not stones:
            return 0
        if len(stones) == 1:
            return stones[0]
        heapq.heapify_max(stones)
        stone1 = heapq.heappop_max(stones)
        stone2 = heapq.heappop_max(stones)
        remaining_stone = abs(stone1 - stone2)
        if remaining_stone > 0:
            heapq.heappush_max(stones, remaining_stone)
        return self.lastStoneWeight(stones)
