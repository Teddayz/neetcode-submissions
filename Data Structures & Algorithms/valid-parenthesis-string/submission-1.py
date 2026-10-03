class Solution:
    def checkValidString(self, s: str) -> bool:
        left_stack = []
        star_stack = []
        for i in range(len(s)):
            if s[i] == "(":
                left_stack.append(i)
            elif s[i] == "*":
                star_stack.append(i)
            else:
                if left_stack:
                    left_stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while left_stack and star_stack:
            left = left_stack.pop()
            right = star_stack.pop()
            if left > right:
                return False
        # If i still have "(", return false
        print(left_stack)
        return len(left_stack) == 0
        