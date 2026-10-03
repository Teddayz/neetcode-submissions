class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        current = ""

        def backtrack(current: str, open: int, close: int) -> None:
            if close > open or open + close > 2 * n:
                return
            if open + close > 2 * n:
                return
            if len(current) == 2 * n and open == close:
                print(current)
                result.append(current)
            
            current += "("
            backtrack(current, open + 1, close)
            current = current[:-1]
            current +=  ")"
            backtrack(current, open, close + 1)

        backtrack(current, 0, 0)
        return result