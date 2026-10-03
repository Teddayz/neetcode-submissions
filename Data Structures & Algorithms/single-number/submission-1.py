class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        freq = Counter(nums)
        for key, value in freq.items():
            if value == 1:
                return key