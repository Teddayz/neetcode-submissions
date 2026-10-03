class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            middle = (left + right) // 2
            # Either this is the start, or the end or in the middle
            if target == nums[middle]:
                temp = middle
                while temp >= 0 and nums[temp] == target:
                    temp -= 1
                res.append(temp + 1)
                temp = middle
                while temp < len(nums) and nums[temp] == target:
                    temp += 1
                res.append(temp - 1)
                return res
            elif target > nums[middle]:
                left = middle + 1
            else:
                right = middle - 1
        return [-1, -1]


