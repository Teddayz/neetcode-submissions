class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Since the numbers is already sorted in non-decreasing order, we can just make use of two pointer indexing
        left, right = 0, len(numbers) - 1
        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left + 1, right + 1]
            elif res < target:
                left += 1
            else:
                right -= 1
        return None