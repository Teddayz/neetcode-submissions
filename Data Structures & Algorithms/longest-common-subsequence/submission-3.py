class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp = [[0] * len(text2) for _ in range(len(text1))]
        def recursive_check(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0
            if dp[i][j] != 0:
                return dp[i][j]
            if text1[i] == text2[j]:
                result = 1 + recursive_check(i + 1, j + 1)
                dp[i][j] = result
                return result
            else:
                result = max(recursive_check(i, j + 1), recursive_check(i + 1, j))
                dp[i][j] = result
                return result
        recursive_check(0, 0)
        return dp[0][0]