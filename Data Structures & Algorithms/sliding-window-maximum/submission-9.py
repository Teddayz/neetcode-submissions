import collections
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deq = collections.deque()
        left = right = 0
        output = []
        while right < len(nums):
            while deq and nums[deq[-1]] < nums[right]:
                deq.pop()
            deq.append(right)

            # Out of bounds
            if left > deq[0]:
                deq.popleft()

            if right + 1 >= k:
                output.append(nums[deq[0]])
                left += 1
            right += 1
        return output