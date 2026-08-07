class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Iterate from the left to the right
        # If its height is increasing, we continue to add to the stack
        # Else we take that index as the right boundary, loop through from that index all the way to the left 
        heights.append(0)
        maxArea = 0
        stack = []
        # Add first index
        stack.append(0)
        for i in range(1, len(heights)):
            # print(stack)
            currHeight = heights[i]
            if currHeight < heights[stack[-1]]:
                while stack and currHeight < heights[stack[-1]]:
                    index = stack.pop()
                    height_to_use = heights[index]
                    width = i - stack[-1] - 1 if stack else i
                    area = width * height_to_use
                    maxArea = max(area, maxArea)
            stack.append(i)
            # print(stack)
        return maxArea
            