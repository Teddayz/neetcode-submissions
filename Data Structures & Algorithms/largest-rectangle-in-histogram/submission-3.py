class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        maxArea = 0
        stack = []
        right_boundaries = []
        for i in range(len(heights)):
            if i == 0:
                stack.append(i)
                continue
            currHeight = heights[i]
            if currHeight >= heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and currHeight < heights[stack[-1]]:
                    most_left = stack.pop()
                    if not stack:
                        width = i
                    else:
                        width = (i - stack[-1]) - 1
                    area = width * heights[most_left]
                    maxArea = max(area, maxArea)
                stack.append(i)
        return maxArea
