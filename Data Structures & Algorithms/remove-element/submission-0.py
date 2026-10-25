class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        result = list(filter(lambda x: x != val, nums))
        for i in range(len(result)):
            nums[i] = result[i]
        return len(result)