class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFF

        while b != 0:
            temp = ((a & b) << 1) & MASK
            a = (a ^ b) & MASK
            b = temp
        
        return a if a <= MAX_INT else ~(a ^ MASK)