class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if i == 0:
                stack.append(i)
                continue
            curr = temperatures[i]
            # print(stack[-1])
            while stack and curr > temperatures[stack[-1]]:
                prev_index = stack.pop()
                result[prev_index] = i - prev_index
            # Add current temperature
            stack.append(i)

        return result