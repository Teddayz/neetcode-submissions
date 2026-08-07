import heapq
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        left = 0
        right = 0
        output = []
        pq = []
        while right < len(nums):
            # Initialize to window size < k
            if (right - left + 1) < k:
                heapq.heappush(pq, (-1 * nums[right], right))
                right += 1
                continue
            # Window size == k
            heapq.heappush(pq, (-1 * nums[right], right))
            output.append(pq[0][0] * -1)
            
            pq.remove((-1 * nums[left], left))
            heapq.heapify(pq)

            left += 1
            right += 1
        return output

