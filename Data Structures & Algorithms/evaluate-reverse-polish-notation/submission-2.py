import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_mapping = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": lambda a, b : int(a/b)
        }
        def calculate(num1: str, op_string: str, num2: str) -> int:
            op_func = operator_mapping.get(op_string)
            return op_func(int(num1), int(num2))
        
        for token in tokens:
            if token in operator_mapping:
                right = stack.pop()
                left = stack.pop()
                result = calculate(left, token, right)
                stack.append(result)
            else:
                stack.append(token)
        return int(stack.pop()) if stack else 0
