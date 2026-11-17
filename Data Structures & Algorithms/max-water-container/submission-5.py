class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights) - 1
        res = 0

        while left < right:
            curr = 0
            if heights[left] <= heights[right]:
                curr = (right - left) * heights[left]
                left += 1
            else:
                curr = (right - left) * heights[right]
                right -=1
            res = max(curr, res)
            
        return res