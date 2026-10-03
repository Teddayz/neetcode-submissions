class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        n1, n2 = 0, 0
        for s in num1:
            n1 *= 10
            n1 += ord(s) - ord("0")
        for s in num2:
            n2 *= 10
            n2 += ord(s) - ord("0")
        res = n1 * n2

        return str(res)