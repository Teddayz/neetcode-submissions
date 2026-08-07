class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        maxArea = 0
        stack = []
        stack.append(0)
        for i in range(1, len(heights)):
            currHeight = heights[i]
            if currHeight < heights[stack[-1]]:
                while stack and currHeight < heights[stack[-1]]:
                    index = stack.pop()
                    height_to_use = heights[index]
                    width = i - stack[-1] - 1 if stack else i
                    area = width * height_to_use
                    maxArea = max(area, maxArea)
            stack.append(i)
        return maxArea
            