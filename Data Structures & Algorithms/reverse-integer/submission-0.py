class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        x_str = str(x)
        if x_str[0] == "-":
            negative = True
            x_str = x_str[1:]
            
        left = 0
        right = len(x_str) - 1
        while left < right:
            l = x_str[left]
            r = x_str[right]
            x_str = x_str[:left] + r + x_str[left + 1:right] + l + x_str[right + 1:]
            left += 1
            right -= 1
        res = int("".join(x_str))
        if negative:
            res *= -1
            if res < -2**31:
                return 0
        if res > 2**31 - 1:
            return 0
        return res
        
        