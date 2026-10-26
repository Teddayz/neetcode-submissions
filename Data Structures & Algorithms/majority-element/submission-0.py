class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        reference = nums[0]
        count = 1
        for i in range(1, len(nums)):
            if nums[i] == reference:
                count += 1
            else:
                if count == 0:
                    reference = nums[i]
                    count += 1
                else:
                    count -= 1
        return reference