class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0
        fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        slow1 = 0
        while nums[slow1] != nums[slow]:
            slow1 = nums[slow1]
            slow = nums[slow]
        return nums[slow1]