class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        slow, fast = 1, max(piles) # Represents the fastest and slowest rate we can eat the bananas
        
        while slow <= fast:
            mid = (slow + fast) // 2
            time = 0
            for pile in piles:
                time += math.ceil(pile / mid)
            if time > h:
                slow = mid + 1
            else:
                fast = mid - 1
        return slow
