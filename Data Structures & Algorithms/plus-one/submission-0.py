class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        for i in range(len(digits) - 1, -1, -1):
            if i == len(digits) - 1:
                total = digits[i] + 1 + carry
            else:
                total = digits[i] + carry
            if total > 9:
                carry = 1
                digits[i] = total % 10
            else:
                carry = 0
                digits[i] = total
        if carry == 1:
            digits.insert(0, 1)
        return digits