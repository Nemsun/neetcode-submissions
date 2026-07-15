class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        ops = "+*-/"
        for c in tokens:
            if c not in ops:
                stack.append(int(c))
                continue
            else:
                a, b = stack.pop(), stack.pop()
                if c == "+":
                    stack.append(a + b)
                    continue
                if c == "-":
                    stack.append(b - a)
                    continue
                if c == "*":
                    stack.append(a * b)
                    continue
                if c == "/":
                    stack.append(int(b / a))
                    continue
        return stack.pop()