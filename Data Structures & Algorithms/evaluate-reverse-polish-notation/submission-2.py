class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        math_stack = []
        math_symbols = "+-*/"
        for c in tokens:
            if c not in math_symbols:
                math_stack.append(int(c))
            else:
                num_1 = math_stack.pop()
                num_2 = math_stack.pop()
                if c == '+':
                    math_stack.append(num_2 + num_1)
                elif c == '-':
                    math_stack.append(num_2 - num_1)
                elif c == '*':
                    math_stack.append(num_2 * num_1)
                else:
                    math_stack.append(int(float(num_2) / num_1))
        return math_stack[-1]
        
