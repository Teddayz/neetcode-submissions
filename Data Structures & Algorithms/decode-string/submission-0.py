class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                word = deque()
                while stack and stack[-1] != "[":
                    curr = stack.pop()
                    word.appendleft(curr)
                word = "".join(word)
                stack.pop()
                k = deque()
                while stack and stack[-1].isnumeric():
                    curr = stack.pop()
                    k.appendleft(curr)
                k = "".join(k)
                current_str = word * int(k)
                stack.append(current_str)

        return "".join(stack)