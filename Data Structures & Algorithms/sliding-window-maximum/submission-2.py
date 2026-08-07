import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()  # Stores indices of candidate maximums
        output = []
        
        for i, num in enumerate(nums):
            # 1. Pop smaller elements from the back (they can never be max)
            while q and nums[q[-1]] <= num:
                q.pop()
                
            # 2. Add current element's index
            q.append(i)
            
            # 3. Remove index from front if it's outside the sliding window
            if q[0] <= i - k:
                q.popleft()
                
            # 4. Append current window's max to output (starts once window reaches size k)
            if i >= k - 1:
                output.append(nums[q[0]])
                
        return output

