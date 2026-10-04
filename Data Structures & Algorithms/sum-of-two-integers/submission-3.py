class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF
        MAX_INT = 0x7FFFFFFF
        
        while b != 0:
            # Sum without carry
            sum_without_carry = (a ^ b) & MASK
            # Carry shifted left
            carry = ((a & b) << 1) & MASK
            
            a = sum_without_carry
            b = carry
            
        return a if a <= MAX_INT else ~(a ^ MASK)