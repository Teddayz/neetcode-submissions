import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operator_mapping = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
        }
        def calculate(num1, op_string, num2):
            op_func =     operator_mapping.get(op_string)
            if op_string == "/":
                return int(num1/num2)
            return op_func(num1, num2)
        for token in tokens:
            if token in operator_mapping:
                right = int(stack.pop())
                left = int(stack.pop())
                # Perform arithmetic
                result = calculate(left, token, right)
                # Add back to stack
                stack.append(result)
                
            else:
                stack.append(token)
        if not stack:
            return 0     
        return int(stack.pop())