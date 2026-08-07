class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {')': '(', '}': '{', ']': '['}
        open_characters = ['(', '{', '[']
        stack = []
        for i in range(len(s)):
            if s[i] in open_characters:
                stack.append(s[i])
            else:
                # Close bracket
                char_to_remove = char_map.get(s[i])
                if not stack or stack[-1] != char_to_remove:
                    return False
                else:
                    stack.pop()
        return len(stack) == 0