class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            middle = (left + right) // 2
            # Either this is the start, or the end or in the middle
            if target == nums[middle]:
                res.append(self.smallestBinarySearch(nums, left, middle, target))
                res.append(self.biggestBinarySearch(nums, middle, right, target))
                return res
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return [-1, -1]

    def biggestBinarySearch(self, nums: List[int], start: int, end: int, target: int) -> int:
        ans = -1
        while start <= end:
            middle = (start + end) // 2
            if target == nums[middle]:
                ans = middle
                start = middle + 1
            elif target > nums[middle]:
                start = middle + 1
            else:
                end = middle - 1
        return ans

    def smallestBinarySearch(self, nums: List[int], start: int, end: int, target: int) -> int:
        ans = -1
        while start <= end:
            middle = (start + end) // 2
            if target == nums[middle]:
                ans = middle
                end = middle - 1
            elif target > nums[middle]:
                start = middle + 1
            else:
                end = middle - 1
        return ans



