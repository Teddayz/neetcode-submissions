class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        digitMap = {
            '2': ['a', 'b', 'c'], '3': {'d', 'e', 'f'}, '4': ['g', 'h', 'i'], 
            '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], 
            '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']
            }
        result = []
        def backtrack(current: str, index: int):
            if len(current) == len(digits):
                result.append(current)
            if index >= len(digits):
                return
            digit = digits[index]
            for char in digitMap.get(digit):
                current += char
                backtrack(current, index + 1)
                current = current[:-1]
            
        backtrack("", 0)
        return result
        