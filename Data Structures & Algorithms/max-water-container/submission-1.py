class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_water = 0

        while left < right:
            curr_water = (right - left) * min(heights[left], heights[right])
            if curr_water > max_water:
                max_water = curr_water
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_water