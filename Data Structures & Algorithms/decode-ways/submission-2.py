class Solution:
    def numDecodings(self, s: str) -> int:
        # Start from the end, if can decode then add one
        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            elif i + 1 < len(s) and (s[i] == "1" or (s[i] == "2" and s[i + 1] in "0123456")):
                dp[i] = dp[i + 1] + dp[i + 2]
            else:
                dp[i] = dp[i + 1]
        # print(dp)
        return dp[0]
