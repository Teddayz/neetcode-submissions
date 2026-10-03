class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        digits[len(digits) - 1] += 1
        i = len(digits) - 1
        while i >= 0:
            digits[i] += carry
            if digits[i] > 9:
                carry = 1
                digits[i] = digits[i] % 10
            else:
                carry = 0
            i -= 1
        if carry == 1:
            digits.insert(0, 1)
        return digits