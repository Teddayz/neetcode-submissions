class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[slow]

        while nums[slow] != nums[fast]:
            slow = nums[slow]
            fast = nums[nums[fast]]

        new_slow = 0
        while nums[new_slow] != nums[slow]:
            slow = nums[slow]
            new_slow = nums[new_slow]

        return nums[new_slow]