class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        queue = deque()

        left, right = 0, 0
        output = []
        while right < len(nums):

            while queue and nums[right] > nums[queue[-1]]:
                queue.pop()
            queue.append(right)

            if queue[0] < left:
                queue.popleft()
            
            if right - left + 1 >= k:
                output.append(nums[queue[0]])
                left += 1
            right += 1
        return output
