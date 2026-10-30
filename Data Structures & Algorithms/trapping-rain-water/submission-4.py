class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        i = 0
        res = 0
        # Monotonic decreasing stack
        while i < len(height):
            # print(stack)
            if stack:
                if height[i] < height[stack[-1]]:
                    stack.append(i)
                else:
                    while stack and height[i] >= height[stack[-1]]:
                        prev_index = stack.pop()
                        if stack:
                            width = i - stack[-1] - 1
                            res += width * (min(height[i], height[stack[-1]]) - height[prev_index])
                    stack.append(i)
            else:
                stack.append(i)
            
            i += 1

        return res
            
