class Solution:
    def reverseBits(self, n: int) -> int:
        ans = 0
        for i in range(32):
            mask = n & 1
            n = n >> 1
            ans = ans | mask
            ans = ans << 1
            # print(ans)
        return ans >> 1